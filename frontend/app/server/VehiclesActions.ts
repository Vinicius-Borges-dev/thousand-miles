"use server";

export const addNewVehicle = async (formContent:FormData)=>{
  console.log(formContent)
  try {
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/vehicles/create`, {
      method: "POST",
      body: formContent,
    });
    const data = await response.json();
    return data
  } catch (err) {
    throw new Error("Erro na requisição: " + err);
  }
}


export const getAllVehicles = async () => {
  try {
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/vehicles/`);
    const data = await response.json();
    return data;
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


export const updateVehicle = async (formContent:FormData)=> {
  const id = formContent.get("id");
  try{
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/vehicles/${id}`,{
      method: "PUT",
      body: formContent
    })

    const data = response.json()

    return data

  } catch (err) {
    throw new Error("Erro na requisição: " + err);
  }
}


export const deleteVehicle = async (id: number) => {
  try {
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/vehicles/${id}`, {
      method: "DELETE",
    });
    const data = await response.json();
    return data;
  } catch (err) {
    throw new Error("Erro na requisição: " + err);
  }
}