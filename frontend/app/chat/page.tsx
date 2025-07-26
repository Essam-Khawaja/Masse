"use client";

import { useEffect, useRef, useState } from "react";
import ReactMarkdown from "react-markdown";

export default function ChatPage() {
  const [messages, setMessages] = useState([
    {
      from: "ai",
      text: "Welcome, adventurer. What tale shall we weave today?",
    },
  ]);
  const [asked, setAsked] = useState(false);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef<HTMLDivElement>(null);

  // Scroll to bottom on new message
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  async function sendMessage() {
    if (!input.trim()) return;

    const userMessage = { from: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      if (!asked) {
        const response = await fetch(
          "https://masse.onrender.com/generate-campaign",
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: input }),
          }
        );

        const data = await response.json();
        const aiReply = { from: "ai", text: data.reply };
        setMessages((prev) => [...prev, aiReply]);
        setAsked(true);
      } else {
        const response = await fetch(
          "https://masse.onrender.com/elaborate-campaign",
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: input }),
          }
        );

        const data = await response.json();
        const aiReply = { from: "ai", text: data.reply };
        setMessages((prev) => [...prev, aiReply]);
      }
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          from: "ai",
          text: "⚠️ Something went wrong talking to the dungeon.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="padding-chat flex flex-col justify-center items-center h-screen">
      <div className="flex justify-between w-full">
        <a className="nes-btn" href="/">
          &larr;
        </a>
      </div>
      <h1 className="text-5xl mb-4">AI Dungeon Master</h1>
      <div className="p-10 w-full">
        <section className="nes-container with-title is-dark p-4 min-h-[75vh] max-h-[80vh] flex flex-col">
          <p className="title">Chat</p>

          <div className="flex-1 overflow-y-auto space-y-4 pr-2 custom-scroll">
            {messages.map((msg, idx) => (
              <div
                key={idx}
                className={`${
                  msg.from === "user"
                    ? "flex justify-end"
                    : "flex justify-start"
                } animate-fade-in`}
              >
                {/* {msg.from === "user" ? <></> : <i className="nes-bcrikko"></i>} */}

                <div
                  className={`nes-balloon ${
                    msg.from === "user" ? "from-right" : "from-left"
                  } is-dark separate-chat text-balance lg:max-w-1/2 `}
                >
                  <ReactMarkdown>{msg.text}</ReactMarkdown>
                </div>
              </div>
            ))}
            {loading && (
              <div className="flex justify-start animate-fade-in">
                <div className="nes-balloon from-left is-dark p-2">
                  <p>Typing...</p>
                </div>
              </div>
            )}
            <div ref={chatEndRef} />
          </div>

          {/* Input */}
          <div className="mt-4 flex items-center gap-2">
            <input
              type="text"
              className="nes-input w-full"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
              placeholder="Type your message..."
            />
            <button
              className="nes-btn is-primary"
              onClick={sendMessage}
              disabled={loading}
            >
              Send
            </button>
          </div>
        </section>
      </div>
    </div>
  );
}
