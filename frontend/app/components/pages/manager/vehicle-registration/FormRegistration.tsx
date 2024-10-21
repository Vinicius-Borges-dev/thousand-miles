"use client";

import Image from "next/image";
import { useState, useCallback } from "react";
import { useThisToaster } from "@components/toaster/ToasterContext";
import { addNewVehicle } from "@root/app/server/VehiclesActions";

export default function FormRegistration() {
  const [FormInputTextValues, setFormInputTextValues] = useState({
    brand: "",
    model: "",
    category: "",
    year: "",
    color: "",
    pricePerDay: "",
    transmission: "",
    seats: "",
    description: "",
  });

  const [formInputFiles, setFormInputFiles] = useState({
    apresentationPhoto: {
      file: null,
      preview: "",
    },
    lateralPhoto: {
      file: null,
      preview: "",
    },
  });

  const toast = useThisToaster();

  const [error, setError] = useState<string>("");

  const handleStringsInputsChange = (
    e: React.ChangeEvent<
      HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement
    >
  ) => {
    setFormInputTextValues({
      ...FormInputTextValues,
      [e.target.name]: e.target.value,
    });
  };

  const validateForm = () => {
    if (
      FormInputTextValues.brand === "" ||
      FormInputTextValues.model === "" ||
      FormInputTextValues.category === "" ||
      FormInputTextValues.year === "" ||
      FormInputTextValues.color === "" ||
      FormInputTextValues.pricePerDay === ""
    ) {
      setError("Preencha todos os campos!");
      return false;
    }
    return true;
  };

  const handleImageChange = useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      const file = event.target.files?.[0];
      const name = event.target.name;
      if (file) {
        const reader = new FileReader();
        reader.onload = (e: ProgressEvent<FileReader>) => {
          setFormInputFiles((prevState) => ({
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

  const submitForm = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (validateForm()) {
      const formData = new FormData();

      Object.keys(FormInputTextValues).forEach((key) => {
        formData.append(
          key,
          FormInputTextValues[key as keyof typeof FormInputTextValues]
        );
      });

      formData.append(
        "apresentationPhoto",
        formInputFiles.apresentationPhoto.file
      );
      formData.append("lateralPhoto", formInputFiles.lateralPhoto.file);

      const result = await addNewVehicle(formData);

      if (result.status == "ok") {
        toast.success(result.message);

        setFormInputTextValues({
          brand: "",
          model: "",
          category: "",
          year: "",
          color: "",
          pricePerDay: "",
          transmission: "",
          seats: "",
          description: "",
        });

        setFormInputFiles({
          apresentationPhoto: {
            file: null,
            preview: "",
          },
          lateralPhoto: {
            file: null,
            preview: "",
          },
        });
      } else {
        toast.error(result.message);
      }
    } else {
      setError("Preencha todos os campos!");
    }
  };

  return (
    <div className="bg-card-form p-3 rounded-md">
      <h1 className="text-2xl font-open-sans text-center">
        Registro de novo veiculo
      </h1>
      <form
        onSubmit={submitForm}
        className="*:font-open-sans font-semibold tracking-wide"
        encType="multipart/form-data"
      >
        <div className="lg:flex">
          <div className="w-full px-2 [&>div>input]:w-full [&>div>div>input]:w-full [&>div>div>select]:w-full [&>div>div>select]:bg-input [&>div>div>select]:rounded-lg [&>div>input]:bg-input [&>div>div>input]:bg-input [&>div>input]:rounded-lg [&>div>div>input]:rounded-lg [&>div>textarea]:w-full [&>div>textarea]:bg-input [&>div>textarea]:rounded-lg">
            <div className="mb-6">
              <label htmlFor="brand">Marca do veículo:</label>
              <input
                type="text"
                name="brand"
                id="brand"
                placeholder="Ex.BMW"
                className="pl-[8px] py-[6px]"
                onChange={handleStringsInputsChange}
                required
                value={FormInputTextValues.brand}
              />
            </div>
            <div className="mb-6">
              <label htmlFor="model">Modelo do veículo:</label>
              <input
                type="text"
                name="model"
                id="model"
                placeholder="Ex.I8"
                className="pl-[8px] py-[6px]"
                onChange={handleStringsInputsChange}
                required
                value={FormInputTextValues.model}
              />
            </div>
            <div className="mb-6">
              <label htmlFor="category">Categoria do veículo:</label>
              <input
                type="text"
                name="category"
                id="category"
                placeholder="Ex.Esportivo"
                className="pl-[8px] py-[6px]"
                onChange={handleStringsInputsChange}
                required
                value={FormInputTextValues.category}
              />
            </div>
            <div className="mb-6">
              <label htmlFor="year">Ano do veículo:</label>
              <input
                type="number"
                min={1966}
                max={new Date().getFullYear() + 1}
                name="year"
                id="year"
                placeholder="Ex.2020"
                className="pl-[8px] py-[6px]"
                onChange={handleStringsInputsChange}
                required
                value={FormInputTextValues.year}
              />
            </div>
            <div className="mb-6">
              <label htmlFor="color">Cor do veículo:</label>
              <input
                type="text"
                name="color"
                id="color"
                placeholder="Ex.Vermelho"
                className="pl-[8px] py-[6px]"
                onChange={handleStringsInputsChange}
                required
                value={FormInputTextValues.color}
              />
            </div>
            <div className="mb-6">
              <label htmlFor="pricePerDay">Preço por dia:</label>
              <input
                type="text"
                name="pricePerDay"
                id="pricePerDay"
                placeholder="Ex.BMW"
                className="pl-[8px] py-[6px]"
                onChange={handleStringsInputsChange}
                required
                value={FormInputTextValues.pricePerDay}
              />
            </div>
            <div className="flex w-full gap-4">
              <div className="mb-6 w-1/2">
                <label htmlFor="transmission">Tipo de câmbio:</label>
                <select
                  name="transmission"
                  id="transmission"
                  defaultValue={"Manual"}
                  className="p-2"
                  onChange={handleStringsInputsChange}
                >
                  <option value="Manual">Manual</option>
                  <option value="Automatic">Automático</option>
                </select>
              </div>
              <div className="mb-6 w-1/2">
                <label htmlFor="seats">Número de assentos:</label>
                <input
                  type="number"
                  max={7}
                  min={1}
                  name="seats"
                  id="seats"
                  placeholder="Ex.2"
                  className="p-2"
                  onChange={handleStringsInputsChange}
                  required
                  value={FormInputTextValues.seats}
                />
              </div>
            </div>
            <div className="mb-6">
              <label htmlFor="description">Descrição:</label>
              <textarea
                name="description"
                id="description"
                placeholder="Ex.Veículo esportivo com assentos de couro, pintura interna e externa em perfeito estado."
                className="pl-[8px] py-[6px] h-[100%_!important] resize-none"
                onChange={handleStringsInputsChange}
                rows={13}
                value={FormInputTextValues.description}
                required
              ></textarea>
            </div>
          </div>
          <div className="w-full flex flex-col justify-between">
            <div className="mb-6">
              <label htmlFor="apresentationPhoto">Foto de apresentação:</label>
              <Image
                src={
                  formInputFiles.apresentationPhoto.preview ||
                  "https://placehold.co/500x200.svg"
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
                onChange={handleImageChange}
                required
              />
            </div>
            <div className="mb-6">
              <label htmlFor="lateralPhoto">Foto lateral:</label>
              <Image
                src={
                  formInputFiles.lateralPhoto.preview ||
                  "https://placehold.co/500x200.svg"
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
                onChange={handleImageChange}
                required
              />
            </div>
          </div>
        </div>
        <button
          type="submit"
          className="w-full bg-blue-400 p-3 rounded-lg text-2xl"
        >
          Enviar
        </button>
      </form>
      {error && error !== "" && (
        <p className="text-red-500 text-center">{error}</p>
      )}
    </div>
  );
}
