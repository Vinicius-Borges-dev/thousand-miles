import { useCallback, useEffect, useState } from "react";
import Input from "./Input";
import Image from "next/image";
import {
  getVehicleByIdService,
  updateVehicle,
} from "@root/app/server/VehiclesActions";
import { useThisToaster } from "@components/toaster/ToasterContext";

type EditVehiclesProps = {
  id: number;
};

export default function EditVehicle({ id }: EditVehiclesProps) {
  const toast = useThisToaster();
  const [responseInputData, setResponseInputData] = useState({
    id: id,
    model: "",
    brand: "",
    category: "",
    year: 0,
    color: "",
    price_per_day: 0.0,
    transmission: "",
    seats: "",
    description: "",
  });

  type FileState = {
    isNew: boolean;
    file: File | null;
    preview: string;
  };

  type ResponseFilesType = {
    apresentationPhoto: FileState;
    lateralPhoto: FileState;
  };

  const [ResponseFiles, setResponseFiles] = useState<ResponseFilesType>({
    apresentationPhoto: {
      isNew: false,
      file: null,
      preview: "",
    },
    lateralPhoto: {
      isNew: false,
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
      transmission: vehicle.transmission,
      seats: vehicle.seats,
      description: vehicle.description,
    }));
    setResponseFiles((prevState) => ({
      ...prevState,
      apresentationPhoto: {
        isNew: false,
        file: null,
        preview: vehicle.apresentation_photo,
      },
      lateralPhoto: {
        isNew: false,
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
              isNew: true,
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

  const submitForm = useCallback(
    async (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();

      const formData = new FormData();

      Object.keys(responseInputData).forEach((key) => {
        formData.append(
          key,
          String(responseInputData[key as keyof typeof responseInputData])
        );
      });

      if (ResponseFiles.apresentationPhoto.file) {
        formData.append(
          "apresentationPhoto",
          ResponseFiles.apresentationPhoto.file
        );
      }
      if (ResponseFiles.lateralPhoto.file) {
        formData.append("lateralPhoto", ResponseFiles.lateralPhoto.file);
      }

      const result = await updateVehicle(formData);

      if (result.status === "ok") {
        toast.success(result.message, {
          duration: 2000,
        });
        setTimeout(()=>{
          window.location.reload();
        },2000)
      } else {
        toast.error(result.message);
      }
    },
    [responseInputData, ResponseFiles, toast]
  );

  return (
    <form onSubmit={submitForm} className="h-[500px] overflow-auto">
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
          <div className="flex gap-4">
            <div className="w-1/2 mt-5">
              <label
                htmlFor="transmission"
                className="font-bold tracking-wide text-nowrap"
              >
                Tipo de câmbio:
              </label>
              <select
                name="transmission"
                id="transmission"
                className="w-full h-[40px] p-2 bg-input rounded-lg outline-none focus:border focus:border-blue-400 font-semibold mt-2"
                onChange={handleChangeInput}
                value={responseInputData.transmission}
              >
                <option value="Manual">Manual</option>
                <option value="Automatic">Automático</option>
              </select>
            </div>
            <div className="w-1/2">
              <Input
                label="Número de assentos:"
                name="seats"
                onChange={handleChangeInput}
                type="number"
                placeholder="Digite número de assentos."
                value={responseInputData.seats}
              />
            </div>
          </div>
          <Input
            label="Descrição do veículo:"
            name="description"
            onChange={handleChangeInput}
            type="textarea"
            placeholder="Digite a descrição do veículo."
            value={responseInputData.description}
          />
        </div>
        <div className="lg:w-1/2">
          <div className="mb-6">
            <label htmlFor="apresentationPhoto">Foto de apresentação:</label>
            <Image
              src={
                ResponseFiles.apresentationPhoto.isNew === false
                  ? `/api/${ResponseFiles.apresentationPhoto.preview}`
                  : ResponseFiles.apresentationPhoto.preview
              }
              width={500}
              height={500}
              priority
              alt="Apresentation Photo"
              className="rounded-lg w-full h-[350px] object-contain mb-2"
            />
            <input
              type="file"
              name="apresentationPhoto"
              id="apresentationPhoto"
              className="w-full file:bg-input file:rounded-lg file:p-2 file:text-white file:w-full"
              onChange={handleImageChange}
              required
            />
          </div>
          <div className="mb-6">
            <label htmlFor="apresentationPhoto">Foto da lateral:</label>
            <Image
              src={
                ResponseFiles.lateralPhoto.isNew === false
                  ? `/api/${ResponseFiles.lateralPhoto.preview}`
                  : ResponseFiles.lateralPhoto.preview
              }
              width={500}
              height={500}
              priority
              alt="Lateral Photo"
              className="rounded-lg w-full h-[350px] object-contain mb-2"
            />
            <input
              type="file"
              name="lateralPhoto"
              id="lateralPhoto"
              className="w-full file:bg-input file:rounded-lg file:p-2 file:text-white file:w-full"
              onChange={handleImageChange}
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
