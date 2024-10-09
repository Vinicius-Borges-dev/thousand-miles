import type { Metadata } from "next";
import "./globals.css";
import Base from "@components/shared/Base";
import React, { ReactElement } from "react";

export const metadata: Metadata = {
  title: "Thousand Miles",
  description: "Website de locação de veículos de luxo. (Experimental)",
};

export default function RootLayout({children}:{children: ReactElement}): JSX.Element {
  return (
    <html lang="pt-br">
      <body className={`overflow-x-hidden *:text-white`}>
        <Base>{children}</Base>
      </body>
    </html>
  );
}
