import React from "react";
import Footer from "./Footer";
import Navbar from "./Navbar";
import Background from "./Background";

type BaseProps = {
  children: React.ReactNode;
};

export default function Base({ children }: BaseProps) {
  return (
    <>
      <Background />
      <Navbar />
      <main className="min-h-[150vh] container absolute pt-28 left-2/4 -translate-x-2/4">
        {children}
        <Footer />
      </main>
    </>
  );
}
