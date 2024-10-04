"use client";

import React, { ReactElement, useEffect, useRef } from "react";
import Footer from "./Footer";
import Navbar from "./Navbar";
import Background from "./Background";

type BaseProps = {
  children: ReactElement[];
};

export default function Base({ children }: BaseProps) {
  const backgroundRef = useRef<HTMLDivElement | null>(null);
  const mainRef = useRef<HTMLDivElement | null>(null);
  const footerRef = useRef<HTMLDivElement | null>(null);
  const childrenRef = useRef<HTMLDivElement | null>(null);

  const resizeBackground = () => {
    const background = backgroundRef.current;
    const main = mainRef.current;
    const footer = footerRef.current;

    if (background && main && footer) {
      const mainHeight = main.offsetHeight;
      const footerHeight = footer.offsetHeight;
      background.style.height = `${mainHeight + footerHeight + 20}px`;
    }
  };

  useEffect(() => {
    resizeBackground();
    
    const children = childrenRef.current;
    console.log(children)
    
  }, [backgroundRef, mainRef, footerRef]);

  const childrenWithRef = React.Children.map(children,(child)=>{
    return React.cloneElement(child as React.ReactElement, { ref: childrenRef });
  });

  return (
    <>
      <Background ref={backgroundRef} />
      <Navbar />
      <main
        className="min-h-[120vh] container absolute pt-28 left-2/4 -translate-x-2/4 z-0"
        ref={mainRef}
      >
        {childrenWithRef}
        <Footer ref={footerRef} />
      </main>
    </>
  );
}
