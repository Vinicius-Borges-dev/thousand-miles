import React, { createContext, useState, useContext, ReactNode } from 'react';
import ModalBase from './ModalBase';

export type ModalContextType = {
  openModal: (content?: JSX.Element) => void;
  closeModal?: ()=> void;
};

const ModalContext = createContext<ModalContextType | undefined>(undefined);

export const ModalProvider = ({ children }: { children: ReactNode }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [modalContent, setModalContent] = useState<JSX.Element | null>(null);

  const openModal = (content?: JSX.Element) => {
    setIsModalOpen(true);
    if (content) setModalContent(content);
  };

  const closeModal = () => setIsModalOpen(false);

  return (
    <ModalContext.Provider value={{openModal, closeModal}}>
      {children}
      {isModalOpen && <ModalBase closeModal={closeModal}>{modalContent}</ModalBase>}
    </ModalContext.Provider>
  );
};

export const useModal = (): ModalContextType => {
  const context = useContext(ModalContext);
  if (context === undefined) {
    throw new Error("Erro");
  }
  return context;
};
