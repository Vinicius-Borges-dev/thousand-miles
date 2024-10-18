"use client";
import TableContainer from "@components/shared/TableContainer";
import { useModal } from "@components/modal/BaseModal/ModalContext";
import { useState, useEffect, useCallback } from "react";
import { getVehiclesService } from "@root/app/server/ServerActions";

const ManagerVehicles = () => {
  const { openModal } = useModal();
  const [content, setContent] = useState([]);

  const getVehicles = useCallback(async() => {
    const result = await getVehiclesService();
    setContent(result);
  }, []);

  useEffect(() => {
    getVehicles();
  }, [getVehicles]);

  return (
    <TableContainer
      keys={[
        "id",
        "modelo",
        "marca",
        "categoria",
        "ano",
        "cor",
        "preço por dia",
        "descrição",
        "ações",
      ]}
      content={content}
      typeContent="AllVehicles"
      openModal={openModal}
    />
  );
};

export default ManagerVehicles;
