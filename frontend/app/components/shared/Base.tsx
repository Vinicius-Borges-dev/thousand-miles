"use client";

import React, { useEffect, useRef } from "react";
import Footer from "./Footer";
import Navbar from "./Navbar";
import Background from "./Background";
import Table from "@components/shared/Table";

type BaseProps = {
  children: React.ReactNode;
};

export default function Base({ children }: BaseProps) {
  const backgroundRef = useRef<HTMLDivElement | null>(null);
  const mainRef = useRef<HTMLDivElement | null>(null);
  const tableRef = useRef<HTMLTableElement | null>(null);

  useEffect(() => {
    const background = backgroundRef.current;
    const main = mainRef.current;
    const table = tableRef.current;

    if (background && main) {
      const mainHeight = main.offsetHeight;
      background.style.height = `${mainHeight}px`;
    }

    if (table) {
      const tableHeight = table.offsetHeight;
      console.log("Height of Table:", tableHeight);
    }
  }, [backgroundRef, mainRef]);

  return (
    <>
      <Background ref={backgroundRef} />
      <Navbar />
      <main
        className="min-h-[120vh] container absolute pt-28 left-2/4 -translate-x-2/4"
        ref={mainRef}
      >
        {React.Children.map(children, (child) => {
          if (React.isValidElement(child) && child.type === Table) {
            return React.cloneElement(child, { ref: tableRef });
          }
          return child;
        })}
        <Footer />
      </main>
    </>
  );
}
