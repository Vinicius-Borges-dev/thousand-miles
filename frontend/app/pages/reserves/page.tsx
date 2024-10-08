import TableContainer from "@root/app/components/shared/TableContainer";
import HeaderMyReserves from "@components/pages/reserves/HeaderMyReserves";

export default function Reserves() {
  const dataTable: string[] = [
    "Carro",
    "Marca",
    "Tipo",
    "preço por dia",
    "preço total",
    "status",
    "Ações",
  ];

  const content: Array<Array<string | number>> = [
    ["I8", "BMW", "Esportivo", 500.0, 1500.0, "ativo", "cancelar"],
    ["I8", "BMW", "Esportivo", 500.0, 1500.0, "pendente", "cancelar"],
    ["I8", "BMW", "Esportivo", 500.0, 1500.0, "cancelado", ""],
  ];

  return (
    <>
      <HeaderMyReserves />
      <TableContainer keys={dataTable} content={content} />
    </>
  );
}
