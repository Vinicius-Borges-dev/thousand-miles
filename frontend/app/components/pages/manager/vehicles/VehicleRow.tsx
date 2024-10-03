import Image from "next/image";
import bmwCinza from "@images/bmw-cinza.png";
import iconEdit from "@icons/iconEdit.svg";
import iconDelete from "@icons/iconTrash.svg";
import Link from "next/link";
import { Key } from "react";

type VehicleRowProps = {
  model: string;
  vehicleBrand: string;
  category: string;
  pricePerDay: GLfloat;
  amount: number;
  key: Key;
};

export default function VehicleRow({
  model,
  vehicleBrand,
  category,
  pricePerDay,
  amount,
  key,
}: VehicleRowProps) {
  return (
    <tr className="odd:bg-white even:bg-gray-300" key={key}>
      <td>
        <span className="flex gap-3">
          <Image src={bmwCinza} height={30} alt="Veiculo" />
          <span className="pl-2">{model}</span>
        </span>
      </td>
      <td>{vehicleBrand}</td>
      <td>{category}</td>
      <td>R${pricePerDay.toFixed(2).replace(".", ",")}</td>
      <td>{amount}</td>
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
}
