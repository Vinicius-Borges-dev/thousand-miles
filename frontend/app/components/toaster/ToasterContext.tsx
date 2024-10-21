import { createContext, ReactNode, useContext } from "react";
import toast,{ useToaster, Toast, Toaster } from "react-hot-toast";

type ToasterContextProps = {
  children: ReactNode;
};

const ToasterContext = createContext<null | typeof toast>(null);

export const ToasterProvider = ({ children }: ToasterContextProps) => {
  return (
    <ToasterContext.Provider value={toast}>
      <Toaster
      position="top-right"
      containerClassName="text-2xl"
      toastOptions={{
        success:{
          style:{
            background: "rgb(74 222 128)",
            color: "white",
          },
          iconTheme:{
            primary: "rgb(163 230 53)",
            secondary: "black",
          },
        },
      }}/>
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
