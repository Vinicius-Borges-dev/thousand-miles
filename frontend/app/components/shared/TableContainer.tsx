"use server";

import VehicleRow from "../pages/manager/vehicles/VehicleRow";

type TableContainerProps = {
  keys: string[];
  content: string[];
};

export default async function TableContainer({
  keys,
  content,
}: TableContainerProps) {
  console.log(content);
  return (
    <div className="">
      <table className="w-full *:font-open-sans mt-12">
        <thead className="[&>tr>th]:text-left [&>tr>th]:pl-2 [&>tr>th]:pb-4 *:uppercase *:font-bold">
          <tr>
            {keys.map((content, index) => {
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
          {/* {content.map((item, index) => {
            return <VehicleRow />;
          })} */}
          {Array.from({ length: 25 }).map((_, index) => {
            return (
              <VehicleRow
                model="I8"
                vehicleBrand="BMW"
                category="Esportivo"
                pricePerDay={100.0}
                amount={54}
                key={index}
              />
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
