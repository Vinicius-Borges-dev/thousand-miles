import type { Metadata } from "next";
import "./globals.css";
import Base from "@components/shared/Base";

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
      <body className={`overflow-x-hidden`}>
        <Base>{children}</Base>
      </body>
    </html>
  );
}
