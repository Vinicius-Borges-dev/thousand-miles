import { createContext, ReactNode, useContext } from "react";
import toast, { Toaster } from "react-hot-toast";

type ToasterContextProps = {
  children: ReactNode;
};

const ToasterContext = createContext<null | typeof toast>(null);

export const ToasterProvider = ({ children }: ToasterContextProps) => {
  return (
    <ToasterContext.Provider value={toast}>
      <Toaster
        position="top-center"
        containerClassName="text-2xl"
        gutter={10}
        toastOptions={{
          className: "mt-10",
          success: {
            style: {
              background: "white",
              color: "black",
            },
            iconTheme: {
              primary: "rgb(163 230 53)",
              secondary: "white",
            },
          },
        }}
      />
      {children}
    </ToasterContext.Provider>
  );
};

export const useThisToaster = () => {
  const context = useContext(ToasterContext);
  if (context === null) {
    throw new Error("Erro no toaster");
  }
  return context;
};
