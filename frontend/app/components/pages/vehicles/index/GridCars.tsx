"use client";

import { getAllVehicles } from "@server/VehiclesActions";
import CardCars from "./CardCar";
import { useCallback, useEffect, useState, useContext, ReactNode } from "react";
import { VeiculosContext } from "@root/app/pages/vehicles/index/page";

type VehicleType = {
  id: number;
  model: string;
  price: number;
  transmission: string;
  seats: number;
  lateral_photo: string;
};

export default function GridCars() {
  const search = useContext(VeiculosContext);

  const [carsList, setcarsList] = useState<VehicleType[]>([]);

  const fetchVehicles = useCallback(async () => {
    const result = await getAllVehicles();
    if (result.status === "ok") {
      const vehicles = result.data.map((vehicle: VehicleType) => ({
        id: vehicle.id,
        model: vehicle.model,
        price: vehicle.price_per_day,
        transmission: vehicle.transmission,
        seats: Number(vehicle.seats),
        lateral_photo: vehicle.lateral_photo,
      }));
      setcarsList(vehicles);
    }
  }, []);

  useEffect(() => {
    fetchVehicles();
  }, [fetchVehicles]);

  return (
    <section className="grid grid-cols-4 gap-4 mt-20">
      {carsList.map((car: VehicleType) => (
        <CardCars
          key={car.id}
          id={car.id}
          model={car.model}
          price={car.price}
          transmission={car.transmission}
          seats={car.seats}
          lateral_photo={car.lateral_photo}
        />
      ))}
    </section>
  );
}
