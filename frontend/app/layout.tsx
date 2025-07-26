import type { Metadata } from "next";
import { Press_Start_2P } from "next/font/google";
import "./globals.css";
// import "nes.css/css/nes.min.css";

const pressStart2P = Press_Start_2P({
  weight: "400",
  subsets: ["latin"],
  variable: "--font-pixel",
});

import { VT323 } from "next/font/google";

const vt323 = VT323({
  weight: "400",
  subsets: ["latin"],
  variable: "--font-retro",
});

export const metadata: Metadata = {
  title: "AI Dungeon Master",
  description: "Your personalized fantasy adventure generator",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body
        className={`${pressStart2P.variable} ${vt323.variable} font-pixel bg-black text-white`}
      >
        {children}
      </body>
    </html>
  );
}
