"use client";
import TableContainer from "@components/shared/TableContainer";
import { useModal } from "@components/modal/BaseModal/ModalContext";
import { useState, useEffect } from "react";

const ManagerVehicles = () => {
  const { openModal } = useModal();
  const [content, setContent] = useState([]);

  const getVehicles = async () => {
    try {
      const response = await fetch('/api/vehicles/');
      const data = await response.json();
      const vehicles = data.vehicles;

      const newContent = vehicles.map(vehicle => [
        vehicle.id, vehicle.model, vehicle.brand, vehicle.category,
        vehicle.year, vehicle.color, vehicle.price_per_day, vehicle.description
      ]);

      setContent(newContent);
      console.log(content);
    } catch (err) {
      throw new Error('Erro na requisição: ' + err);
    }
  };

  useEffect(() => {
    getVehicles();
  }, []);

  return (
    <TableContainer
      keys={[
        "id", "modelo", "marca", "categoria",
        "ano", "cor", "preço por dia", "descrição"
      ]}
      content={content}
      typeContent="AllVehicles"
      openModal={openModal}
    />
  );
};

export default ManagerVehicles;
