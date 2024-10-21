"use client";
import TableContainer from "@components/shared/TableContainer";
import { useModal } from "@components/modal/BaseModal/ModalContext";
import { useState, useEffect, useCallback } from "react";
import { getVehiclesService } from "@root/app/server/VehiclesActions";

const ManagerVehicles = () => {
  const { openModal } = useModal();
  const [content, setContent] = useState([]);

  const getVehicles = useCallback(async() => {
    const result = await getVehiclesService();
    if (result.status === "ok"){
      const vehicles = result.data;

      type VehicleTypes = {
        id: string;
        model: string;
        brand: string;
        category: string;
        year: number;
        color: string;
        price_per_day: number;
        transmission: string;
        seats: number;
        description: string;
        lateral_photo: string;
      };
  
      const newContent = vehicles.map((vehicle: VehicleTypes) => [
        vehicle.id,
        vehicle.model,
        vehicle.brand,
        vehicle.category,
        vehicle.year,
        vehicle.color,
        vehicle.price_per_day,
        vehicle.transmission,
        vehicle.seats,
        vehicle.description,
        "editar",
        vehicle.lateral_photo,
        "excluir",
      ]);
  
      setContent(newContent);
    }
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
        "tipo de câmbio",
        "número de assentos",
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
