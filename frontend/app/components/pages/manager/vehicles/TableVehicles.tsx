"use server";

import Table from "@root/app/components/shared/Table";
import Image from "next/image";
import bmwCinza from "@images/bmw-cinza.png";
import iconEdit from "@icons/iconEdit.svg";
import iconDelete from "@icons/iconTrash.svg";

export default async function TableVehicles() {
  return (
    <Table>
      <thead className="[&>tr>th]:text-left [&>tr>th]:pl-2">
        <tr>
          <th>Modelo</th>
          <th>Marca</th>
          <th>Categoria</th>
          <th>Preço por dia</th>
          <th>Quantidade de veículos disponiveis</th>
          <th colSpan={2}>Ações</th>
        </tr>
      </thead>
      <tbody className="*:text-black rounded-lg [&>tr>td]:py-3 [&>tr>td]:font-semibold [&>tr>td]:text-tbody-text-color [&>tr>td]:pl-2 [&>tr]:border-[2px] [&>tr]:border-b-table-border">
        <tr className="first:[&>td:first-child]:rounded-tl-lg first:[&>td:last-child]:rounded-tr-lg last:[&>td:first-child]:rounded-bl-lg last:[&>td:last-child]:rounded-br-lg">
    <td>
      <span className="flex gap-3">
        <Image src={bmwCinza} height={30} alt="Veiculo" />
        <span className="pl-2">I8</span>
      </span>
    </td>
    <td>BMW</td>
    <td>Carro</td>
    <td>100,00</td>
    <td>54</td>
    <td>
      <span className="flex gap-3 border border-gray-600 rounded-md p-1 w-fit">
        <Image src={iconEdit} alt="Icone de edição" />
        Editar
      </span>
    </td>
    <td>
      <span className="flex gap-3 border border-gray-600 rounded-md p-1 w-fit">
        <Image src={iconDelete} alt="Icone de edição" />
        Excluir
      </span>
    </td>
  </tr>
      </tbody>
    </Table>
  );
}
