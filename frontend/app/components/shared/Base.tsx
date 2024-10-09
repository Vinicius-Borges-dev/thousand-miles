"use client";

import React, { useEffect, useRef, useState } from "react";
import Footer from "./Footer";
import Navbar from "./Navbar";
import Background from "./Background";
import { usePathname } from "next/navigation";
import ModalBase from "../modal/ModalBase";

type BaseProps = {
  children: React.ReactNode;
};

export default function Base({ children }: BaseProps) {
  const backgroundRef = useRef<HTMLDivElement | null>(null);
  const mainRef = useRef<HTMLDivElement | null>(null);
  const footerRef = useRef<HTMLDivElement | null>(null);
  const pathname = usePathname();
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [modalContent, setModalContent] = useState<JSX.Element | null>(null);

  const openModal = (content?: JSX.Element) => {
    setIsModalOpen(true);
    if (content) {
      setModalContent(content);
    }
  }

  const closeModal = () => {
    setIsModalOpen(false);
  }

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
    <>
      <Background ref={backgroundRef} />
      <Navbar openModal={openModal}/>
      <main
        className="min-h-[120vh] container absolute pt-28 left-2/4 -translate-x-2/4 z-0"
        ref={mainRef}
      >
        {children}
        <Footer ref={footerRef} />
      </main>
      {isModalOpen ? (
        <ModalBase size="sm" closeModal={closeModal}>
          {modalContent}
        </ModalBase>
      ) : (
        ""
      )}
    </>
  );
}
