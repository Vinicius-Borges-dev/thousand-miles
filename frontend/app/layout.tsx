import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Thousand Miles",
  description: "Website de locação de veículos de luxo. (Experimental)",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-br">
      <body
        className={`overflow-x-hidden`}
      >
        {children}
      </body>
    </html>
  );
}
