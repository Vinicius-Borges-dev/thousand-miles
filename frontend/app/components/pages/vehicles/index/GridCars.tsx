"use client";

import { getAllVehicles } from "@server/VehiclesActions";
import CardCars from "./CardCar";
import { useCallback, useEffect, useState } from "react";

export default function GridCars() {
  const [cars, setCars] = useState([]);

  const getVehicles = useCallback(async () => {
    const result = await getAllVehicles();

    if (result.status === "ok") {
      const vehicles = result.data;

      type VehicleType = {
        id: string;
        model: string;
        brand: string;
        category: string;
        year: number;
        price_per_day: number;
        transmission: string;
        seats: number;
        lateral_photo: string;
      };

      const vehiclesMapped = vehicles.map((vehicle: VehicleType) => {
        return {
          id: vehicle.id,
          model: vehicle.model,
          brand: vehicle.brand,
          year: vehicle.year,
          price_per_day: vehicle.price_per_day,
          transmission: vehicle.transmission,
          seats: vehicle.seats,
          lateral_photo: vehicle.lateral_photo,
        };
      });
      setCars(vehiclesMapped);
    }
  }, []);

  useEffect(() => {
    getVehicles();
  }, []);

  return (
    <section className="grid grid-cols-4 gap-4 mt-20">
      {cars.map((car) => {
        return <CardCars key={car.id} />;
      })}
    </section>
  );
}
