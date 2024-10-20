import { useCallback, useEffect, useState } from "react";
import Input from "./Input";
import Image from "next/image";
import { getVehicleByIdService } from "@server/ServerActions";

type EditVehiclesProps = {
  id: number;
};

export default function EditVehicle({ id }: EditVehiclesProps) {
  const [responseInputData, setResponseInputData] = useState({
    id: id,
    model: "",
    brand: "",
    category: "",
    year: 0,
    color: "",
    price_per_day: 0.0,
    description: "",
  });

  const [ResponseFiles, setResponseFiles] = useState({
    apresentationPhoto: {
      file: null,
      preview: "",
    },
    lateralPhoto: {
      file: null,
      preview: "",
    },
  });

  const getVehicleById = useCallback(async (identifier: number) => {
    const vehicle = await getVehicleByIdService(identifier);
    setResponseInputData((prevState) => ({
      ...prevState,
      model: vehicle.model,
      brand: vehicle.brand,
      category: vehicle.category,
      year: vehicle.year,
      color: vehicle.color,
      price_per_day: vehicle.price_per_day,
      description: vehicle.description,
    }));
    setResponseFiles((prevState) => ({
      ...prevState,
      apresentationPhoto: {
        file: null,
        preview: vehicle.apresentation_photo,
      },
      lateralPhoto: {
        file: null,
        preview: vehicle.lateral_photo,
      },
    }));
  }, []);

  useEffect(() => {
    getVehicleById(id);
  }, [getVehicleById, id]);

  const handleChangeInput = useCallback(
    (
      e: React.ChangeEvent<
        HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement
      >
    ) => {
      setResponseInputData((prevState) => ({
        ...prevState,
        [e.target.name]: e.target.value,
      }));
    },
    []
  );


  const handleImageChange = useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      const file = event.target.files?.[0];
      const name = event.target.name;
      if (file) {
        const reader = new FileReader();
        reader.onload = (e: ProgressEvent<FileReader>) => {
          setResponseFiles((prevState) => ({
            ...prevState,
            [name]: {
              file: file,
              preview: e.target?.result,
            },
          }));
        };
        reader.readAsDataURL(file);
      }
    },
    []
  );

  return (
    <form className="h-[500px] overflow-auto">
      <div className="lg:flex lg:gap-3">
        <div className="lg:w-1/2">
          <Input
            label="Modelo do veículo:"
            name="model"
            onChange={handleChangeInput}
            type="text"
            placeholder="Digite o modelo do veículo"
            value={responseInputData.model}
          />
          <Input
            label="Marca do veículo:"
            name="brand"
            onChange={handleChangeInput}
            type="text"
            placeholder="Digite a marca do veículo"
            value={responseInputData.brand}
          />
          <Input
            label="Categoria do veículo:"
            name="category"
            onChange={handleChangeInput}
            type="text"
            placeholder="Digite a categoria do veículo"
            value={responseInputData.category}
          />
          <Input
            label="Ano do veículo:"
            name="year"
            onChange={handleChangeInput}
            type="number"
            placeholder="Digite o ano do veículo"
            value={responseInputData.year}
          />
          <Input
            label="Cor do veículo:"
            name="color"
            onChange={handleChangeInput}
            type="text"
            placeholder="Digite o ano do veículo"
            value={responseInputData.color}
          />
          <Input
            label="Preço por dia:"
            name="price_per_day"
            onChange={handleChangeInput}
            type="text"
            placeholder="Digite o preço do veículo por dia."
            value={responseInputData.price_per_day}
          />
          <Input
            label="Descrição do veículo:"
            name="price_per_day"
            onChange={handleChangeInput}
            type="textarea"
            placeholder="Digite o preço do veículo por dia."
            value={responseInputData.description}
          />
        </div>
        <div className="lg:w-1/2">
          <div className="mb-6">
            <label htmlFor="apresentationPhoto">Foto de apresentação:</label>
            <Image
              src={
                ResponseFiles
                  ? `/api/${ResponseFiles.apresentationPhoto.preview}`
                  : "https://placehold.co/500x200.svg"
              }
              width={100}
              height={100}
              alt="Apresentation Photo"
              className="rounded-lg w-full h-[350px] object-contain mb-2"
              layout="responsive"
            />
            <input
              type="file"
              name="apresentationPhoto"
              id="apresentationPhoto"
              className="w-full file:bg-input file:rounded-lg file:p-2 file:text-white file:w-full"
              onChange={handleChangeInput}
              required
            />
          </div>
          <div className="mb-6">
            <label htmlFor="apresentationPhoto">Foto da lateral:</label>
            <Image
              src={
                ResponseFiles
                  ? `/api/${ResponseFiles.lateralPhoto.preview}`
                  : "https://placehold.co/500x200.svg"
              }
              width={100}
              height={100}
              alt="Lateral Photo"
              className="rounded-lg w-full h-[350px] object-contain mb-2"
              layout="responsive"
            />
            <input
              type="file"
              name="lateralPhoto"
              id="lateralPhoto"
              className="w-full file:bg-input file:rounded-lg file:p-2 file:text-white file:w-full"
              onChange={handleChangeInput}
              required
            />
          </div>
        </div>
      </div>
      <span className="w-full">
        <Input label="Atualizar veículo" type="submit" />
      </span>
    </form>
  );
}
