"use client";

import React, { ReactElement, useEffect, useRef } from "react";
import Footer from "./Footer";
import Background from "./Background";
import { usePathname } from "next/navigation";
import { ModalProvider } from '@root/app/components/modal/BaseModal/ModalContext';
import Navbar from "./Navbar";

type BaseProps = {
  children: ReactElement;
};


export default function Base({ children }: BaseProps): JSX.Element {
  const backgroundRef = useRef<HTMLDivElement | null>(null);
  const mainRef = useRef<HTMLDivElement | null>(null);
  const footerRef = useRef<HTMLDivElement | null>(null);
  const pathname = usePathname();

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
  }, [backgroundRef, mainRef, footerRef, pathname]);

  return (
    <ModalProvider>
      <Background ref={backgroundRef} />
      <Navbar />
      <main
        className="min-h-[120vh] container absolute pt-28 left-2/4 -translate-x-2/4 z-0"
        ref={mainRef}
      >
        {children}
        <Footer ref={footerRef} />
      </main>
    </ModalProvider>
  );
}
