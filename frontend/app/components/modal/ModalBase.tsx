import Image from "next/image";
import iconClose from "@icons/iconClose.svg";

type ModalBaseProps = {
  children: React.ReactNode;
  closeModal: () => void;
};

export default function ModalBase({ children, closeModal }: ModalBaseProps) {
  return (
    <section className="fixed top-0 left-0 w-screen h-full bg-black bg-opacity-65 z-20 p-4">
      <div className="w-full h-full relative">
        <div
          className={`p-5 bg-card-form absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 rounded-lg container`}
        >
          <button
            className="absolute -top-6 -right-6 p-3 bg-card-form-lighter rounded-full"
            onClick={closeModal}
          >
            <Image
              src={iconClose}
              width={30}
              height={30}
              alt="Botão de fechar modal"
              className="invert"
            />
          </button>
          {children}
        </div>
      </div>
    </section>
  );
}
