import { forwardRef } from "react";
import VehicleRow from "../pages/manager/vehicles/VehicleRow";

type TableContainerProps = {
  keys: string[];
  content: Array<Array<string | number>>;
  typeContent: string;
  openModal: (content?: JSX.Element) => void;
};

const TableContainer = forwardRef<
  HTMLTableElement,
TableContainerProps
>(({ keys, content=[], typeContent, openModal}, ref) => {
  return (
    <table className="w-full *:font-open-sans mt-12 overflow-auto" ref={ref}>
      <thead className="[&>tr>th]:text-left [&>tr>th]:pl-2 [&>tr>th]:pb-4 *:uppercase *:font-bold">
        <tr>
          {keys.map((content:string, index:number) => {
            if (content == "ações") {
              return (
                <th key={index} colSpan={2}>
                  {content}
                </th>
              );
            } else {
              return <th key={index}>{content}</th>;
            }
          })}
        </tr>
      </thead>
      <tbody className="*:text-black rounded-lg [&>tr>td]:py-3 [&>tr>td]:font-semibold [&>tr>td]:text-tbody-text-color [&>tr>td]:pl-2">
        {content.map((data:Array<string | number>, index:number) => {
          return <VehicleRow items={data} key={index} typeContent={`${typeContent}`} openModal={openModal}/>          
        })}
      </tbody>
    </table>
  );
});

TableContainer.displayName = "TableContainer";

export default TableContainer;