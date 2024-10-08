import TableContainer from "@components/shared/TableContainer";

const ManagerVehicles = () => {
  const content: Array<Array<string | number>> = [
    ["I8", "BMW", "Esportivo", 500.0, 200, "cancelar"],
    ["I8", "BMW", "Esportivo", 500.0, 200, "cancelar"],
    ["I8", "BMW", "Esportivo", 500.0, 200, "cancelar"],
  ];

  return (
    <TableContainer
      keys={[
        "modelo",
        "marca",
        "categoria",
        "preço por dia",
        "quantidade em estoque",
        "ações",
      ]}
      content={content}
    />
  );
};

export default ManagerVehicles;
