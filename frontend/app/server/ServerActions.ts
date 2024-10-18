"use server";

export const getVehiclesService = async () => {
  try {
    const response = await fetch("http://localhost:5000/vehicles/");
    const data = await response.json();
    const vehicles = data.vehicles;

    type VehicleTypes = {
      id: string;
      model: string;
      brand: string;
      category: string;
      year: number;
      color: string;
      price_per_day: number;
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
      vehicle.description,
      vehicle.lateral_photo,
      "editar",
    ]);

    return newContent;
  } catch (err) {
    throw new Error("Erro na requisição: " + err);
  }
};


export const getVehicleByIdService = async (id: number) => {
  try {
    const response = await fetch(`http://localhost:5000/vehicles/${id}`, {
      method: "GET",
    });
    const data = await response.json();
    const vehicle = data.vehicle;
    return vehicle;
  } catch (err) {
    throw new Error("Erro na requisição: " + err);
  }
};