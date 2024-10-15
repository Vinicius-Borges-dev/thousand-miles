"use client";

import Image from "next/image";
import iconEdit from "@icons/iconEdit.svg";
import iconSuccess from "@icons/IconSuccess.svg";
import iconWarning from "@icons/iconWarning.svg";
import iconDanger from "@icons/iconDanger.svg";
import iconDelete from "@icons/iconTrash.svg";
import Link from "next/link";
import EditReserve from "@components/modal/EditReserve";

type VehicleRowProps = {
  items: Array<string | number>;
  typeContent: string;
  openModal: (content?: JSX.Element) => void;
};

export default function VehicleRow({
  items,
  typeContent,
  openModal,
}: VehicleRowProps) {
  const handleEdit = (id: number) => {
    if (typeContent === "AllReserves") {
      openModal(<EditReserve reserveId={id} />);
    }
  };

  return (
    <tr className="odd:bg-white even:bg-gray-200 odd:hover:bg-gray-300 even:hover:bg-gray-300 transition-all [&>td]:h-[66px] [&>td>span]:flex [&>td>span]:items-center">
      {items.map((item: string | number, index: number) => {
        const lastItem = items[items.length - 1].replace("\\", "/");
        if (index == 1) {
          return (
            <td key={index}>
              <span className="flex gap-3">
                <Image
                  src={`/api/${lastItem}`}
                  width={60}
                  height={30}
                  alt="Veiculo"
                />
                <span className="pl-2">{item}</span>
              </span>
            </td>
          );
        }
        if (item === "ativo") {
          return (
            <td key={index} className="flex gap-1">
              <Image src={iconSuccess} alt="Icone de sucesso" />
              <span>{item}</span>
            </td>
          );
        } else if (item === "pendente") {
          return (
            <td key={index} className="flex gap-1 border item-center">
              <Image src={iconWarning} alt="Icone de sucesso" />
              <span>{item}</span>
            </td>
          );
        } else if (item === "cancelado") {
          return (
            <td key={index} className="flex gap-1">
              <Image src={iconDanger} alt="Icone de sucesso" />
              <span>{item}</span>
            </td>
          );
        } else if (item === "cancelar") {
          return (
            <td key={index}>
              <Link
                href=""
                className="flex gap-2 border border-gray-600 rounded-lg w-fit p-2"
              >
                <Image src={iconDelete} alt="Icone de deletar" />
                {item}
              </Link>
            </td>
          );
        } else if (item === "editar") {
          return (
            <td key={index}>
              <button
                className="flex gap-2 border border-gray-600 rounded-lg w-fit p-2"
                onClick={() => handleEdit(Number(items[0]))}
              >
                <Image src={iconEdit} alt="Icone de editar" />
                {item}
              </button>
            </td>
          );
        } else if (item === "excluir") {
          return (
            <td key={index}>
              <button className="flex gap-2 border border-gray-600 rounded-lg w-fit p-2">
                <Image src={iconDelete} alt="Icone de deletar" />
                {item}
              </button>
            </td>
          );
        } else if (index == items.length - 1) {
          return null;
        }
        return <td key={index}>{item}</td>;
      })}
    </tr>
  );
}
