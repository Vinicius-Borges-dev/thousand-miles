import TableContainer from "@components/shared/TableContainer";
import { forwardRef } from "react";

const ManagerVehicles = forwardRef<HTMLTableElement>((props, ref) => {
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
      ref={ref}
    />
  );
});

ManagerVehicles.displayName = "ManagerVehicles";

export default ManagerVehicles;
