import TableContainer from "@components/shared/TableContainer";

const ManagerVehicles = () => {
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
      content={[""]}
    />
  );
};

export default ManagerVehicles;
