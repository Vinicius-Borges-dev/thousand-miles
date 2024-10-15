"use client";
import TableContainer from "@components/shared/TableContainer";
import { useModal } from "@components/modal/BaseModal/ModalContext";
import { useState, useEffect, useCallback } from "react";

const ManagerVehicles = () => {
  const { openModal } = useModal();
  const [content, setContent] = useState([]);

  const getVehicles = useCallback(async () => {
    try {
      const response = await fetch('/api/vehicles/');
      const data = await response.json();
      const vehicles = data.vehicles;

      type VehicleTypes = {
        id: string,
        model: string,
        brand: string,
        category: string,
        year: number,
        color: string,
        price_per_day: number,
        description: string,
        lateral_photo: string
      }

      const newContent = vehicles.map((vehicle:VehicleTypes) => [
        vehicle.id, vehicle.model, vehicle.brand, vehicle.category,
        vehicle.year, vehicle.color, vehicle.price_per_day, vehicle.description, vehicle.lateral_photo
      ]);

      setContent(newContent);
    } catch (err) {
      throw new Error('Erro na requisição: ' + err);
    }
  },[]);

  useEffect(() => {
    getVehicles();
  }, [getVehicles]);

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
