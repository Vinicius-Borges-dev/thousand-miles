"use client";

import React, { useEffect, useRef } from "react";
import Footer from "./Footer";
import Navbar from "./Navbar";
import Background from "./Background";

type BaseProps = {
  children: React.ReactNode;
};

export default function Base({ children }: BaseProps) {
  const backgroundRef = useRef<HTMLDivElement | null>(null);
  const mainRef = useRef<HTMLDivElement | null>(null);
  const footerRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const background = backgroundRef.current;
    const main = mainRef.current;
    const footer = footerRef.current;

    if (background && main) {
      const mainHeight = main.offsetHeight;
      const footerHeight = footer.offsetHeight;
      background.style.height = `${mainHeight + footerHeight + 20}px`;
    }
  }, [backgroundRef, mainRef.current?.offsetHeight]);

  return (
    <>
      <Background ref={backgroundRef} />
      <Navbar />
      <main
        className="min-h-[120vh] container absolute pt-28 left-2/4 -translate-x-2/4 z-0"
        ref={mainRef}
      >
        {children}
        <Footer ref={footerRef} />
      </main>
    </>
  );
}
