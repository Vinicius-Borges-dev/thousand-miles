import { createContext, ReactNode, useContext } from "react";
import toast, { useToaster, Toast } from "react-hot-toast";

type ToasterContextProps = {
  children: ReactNode;
};

const ToasterContext = createContext<null | typeof toast>(null);

export const ToasterProvider = ({ children }: ToasterContextProps) => {
  const { toasts, handlers } = useToaster();
  const { startPause, endPause, calculateOffset, updateHeight } = handlers;

  return (
    <ToasterContext.Provider value={toast}>
      <div
        onMouseEnter={startPause}
        onMouseLeave={endPause}
        className="fixed top-[8rem] right-16 z-50"
      >
        {toasts
          .filter((toast) => toast.visible)
          .map((toast) => {
            const offset = calculateOffset(toast, {
              reverseOrder: false,
              gutter: 8,
            });

            const ref = (el) => {
              if (el && typeof toast.height !== "number") {
                const height = el.getBoundingClientRect().height;
                updateHeight(toast.id, height);
              }
            };
            return (
              <div
                key={toast.id}
                ref={ref}
                className={`
                absolute
                right-0
                p-3 
                bg-white 
                text-black 
                text-2xl 
                rounded-lg
                `}
                style={{
                  transition: "all 0.5s ease-out",
                  opacity: toast.visible ? 1 : 0,
                  transform: `translateY(${offset}px)`,
                }}
                {...toast.ariaProps}
              >
                {toast.message}
              </div>
            );
          })}
      </div>
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
