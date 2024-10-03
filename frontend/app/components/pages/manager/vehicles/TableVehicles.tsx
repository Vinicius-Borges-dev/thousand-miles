"use server";

import Table from "@root/app/components/shared/Table";
import Image from "next/image";
import bmwCinza from "@images/bmw-cinza.png";
import iconEdit from "@icons/iconEdit.svg";
import iconDelete from "@icons/iconTrash.svg";
import Link from "next/link";

export default async function TableVehicles() {
  return (
    <Table>
      <thead className="[&>tr>th]:text-left [&>tr>th]:pl-2 [&>tr>th]:pb-4 *:uppercase *:font-bold">
        <tr>
          <th>Modelo</th>
          <th>Marca</th>
          <th>Categoria</th>
          <th>Preço por dia</th>
          <th>Quantidade de veículos disponiveis</th>
          <th colSpan={2}>Ações</th>
        </tr>
      </thead>
      <tbody className="*:text-black rounded-lg [&>tr>td]:py-3 [&>tr>td]:font-semibold [&>tr>td]:text-tbody-text-color [&>tr>td]:pl-2">
        {Array.from({ length: 5 }).map((_, index) => {
          return (
            <tr className="odd:bg-white even:bg-gray-300" key={index}>
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
                <Link
                  href={`/`}
                  className="flex gap-3 border border-gray-600 rounded-md p-1 w-fit"
                >
                  <Image src={iconEdit} alt="Icone de edição" />
                  Editar
                </Link>
              </td>
              <td>
                <Link
                  href={`/`}
                  className="flex gap-3 border border-gray-600 rounded-md p-1 w-fit"
                >
                  <Image src={iconDelete} alt="Icone de edição" />
                  Excluir
                </Link>
              </td>
            </tr>
          );
        })}
      </tbody>
    </Table>
  );
}
