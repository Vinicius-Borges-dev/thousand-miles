import { useCallback, useEffect, useState } from "react";
import Input from "./Input";

type EditVehiclesProps = {
  id: number;
};

export default function EditVehicle({ id }: EditVehiclesProps) {
  const [ResponseData, setResponseData] = useState({
    id: id,
    model: "",
    brand: "",
    category: "",
    year: 0,
    color: "",
    price_per_day: 0,
  });
  const getVehicleById = useCallback(async (id: number) => {
    try {
      const response = await fetch(`/api/vehicles/${id}`, {
        method: "GET",
      });
      const data = await response.json();
      const vehicle = data.vehicle;

      setResponseData({
        id: vehicle.id,
        model: vehicle.model,
        brand: vehicle.brand,
        category: vehicle.category,
        year: vehicle.year,
        color: vehicle.color,
        price_per_day: vehicle.price_per_day,
      });
    } catch (err) {
      throw new Error("Erro na requisição: " + err);
    }
  }, []);
  useEffect(() => {
    getVehicleById(id);
  }, [getVehicleById, id]);

  const handleChangeInput = useCallback(
    (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
      setResponseData({
        ...ResponseData,
        [e.target.name]: e.target.value,
      });
    },
    [ResponseData]
  );

  return (
    <div>
      <Input
        label="Modelo do veículo:"
        name="model"
        onChange={handleChangeInput}
        type="text"
        placeholder="Digite o modelo do veículo"
        value={ResponseData.model}
      />
      <Input
        label="Marca do veículo:"
        name="brand"
        onChange={handleChangeInput}
        type="text"
        placeholder="Digite a marca do veículo"
        value={ResponseData.model}
      />
      <Input
        label="Categoria do veículo:"
        name="category"
        onChange={handleChangeInput}
        type="text"
        placeholder="Digite a categoria do veículo"
        value={ResponseData.category}
      />
    </div>
  );
}
