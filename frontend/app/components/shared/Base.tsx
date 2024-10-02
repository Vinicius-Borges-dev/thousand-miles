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

  useEffect(()=>{
    const background = backgroundRef.current;
    const main = mainRef.current;

    if(background && main){
      const mainHeight = main.offsetHeight;
      background.style.height = `${mainHeight}px`;
    }
  },[backgroundRef, mainRef]);

  return (
    <>
      <Background ref={backgroundRef} />
      <Navbar />
      <main
        className="min-h-[120vh] container absolute pt-28 left-2/4 -translate-x-2/4"
        ref={mainRef}
      >
        {children}
        <Footer />
      </main>
    </>
  );
}
