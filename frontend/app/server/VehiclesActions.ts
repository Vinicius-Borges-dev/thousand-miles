"use server";

export const addNewVehicle = async (formContent:FormData)=>{
  try {
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/create`, {
      method: "POST",
      body: formContent,
    });
    const data = await response.json();
    return data
  } catch (err) {
    throw new Error("Erro na requisição: " + err);
  }
}


export const getVehiclesService = async () => {
  try {
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/vehicles/`);
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
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/vehicles/${id}`, {
      method: "GET",
    });
    const data = await response.json();
    const vehicle = data.vehicle;
    vehicle.apresentation_photo = vehicle.apresentation_photo.replace("\\","/")
    vehicle.lateral_photo = vehicle.lateral_photo.replace("\\","/")
    return vehicle;
  } catch (err) {
    throw new Error("Erro na requisição: " + err);
  }
};