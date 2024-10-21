import { createContext, ReactNode, useContext } from "react";
import toast,{ Toaster } from "react-hot-toast";

type ToasterContextProps = {
  children: ReactNode;
};

const ToasterContext = createContext<null | typeof toast>(null);

export const ToasterProvider = ({ children }: ToasterContextProps) => {
  console.log("ToasterProvider montado");
  return (
    <ToasterContext.Provider value={toast}>
      <Toaster
      position="top-center"
      containerClassName="text-2xl"
      gutter={10}
      toastOptions={{
        className:"mt-10",
        success:{
          style:{
            background: "white",
            color: "black",
          },
          iconTheme:{
            primary: "rgb(163 230 53)",
            secondary: "white",
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
    console.log("Toaster é nulo");
    throw new Error("Erro no toaster");
  }
  return context;
};
