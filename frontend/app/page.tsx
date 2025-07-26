import Link from "next/link";

export default function Home() {
  return (
    <main className="w-full h-screen flex flex-col justify-center items-center relative overflow-hidden">
      <div className="animate-in delay-100 mb-[3rem] text-center px-4">
        <h1 className="text-4xl md:text-5xl mb-4">🧙‍♂️ AI Dungeon Master</h1>
        <p className="text-md md:text-lg text-gray-300 max-w-xl">
          Embark on a pixel-powered journey. Your fantasy adventure begins with
          a single click.
        </p>
      </div>

      <div className="animate-in delay-300">
        <Link href="/chat">
          <button className="nes-btn is-success text-sm px-6 py-3">
            Start Adventure
          </button>
        </Link>
      </div>
    </main>
  );
}
