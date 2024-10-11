"use client";

import Image from "next/image";
import { useState, useCallback, FormEvent } from "react";

export default function FormRegistration() {
  const [FormInputTextValues, setFormInputTextValues] = useState({
    brand: "",
    model: "",
    category: "",
    year: "",
    color: "",
    pricePerDay: "",
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

  const [error, setError] = useState<string>("");

  const handleStringsInputsChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
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

      try {
        const response = await fetch("/api/vehicles/create", {
          method: "POST",
          body: formData,
        });
        const data = await response.json();

        console.log(data);
      } catch (err: unknown) {
        console.error("Erro no fetch:", err);
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
          <div className="w-full px-2 [&>div>input]:w-full [&>div>input]:bg-input [&>div>input]:rounded-lg [&>div>textarea]:w-full [&>div>textarea]:bg-input [&>div>textarea]:rounded-lg">
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
                type="text"
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
            <div className="mb-6">
              <label htmlFor="description">Descrição:</label>
              <textarea
                name="description"
                id="description"
                placeholder="Ex.Veículo esportivo com assentos de couro, pintura interna e externa em perfeito estado."
                className="pl-[8px] py-[6px]"
                onChange={handleStringsInputsChange}
                value={FormInputTextValues.description}
                required
              ></textarea>
            </div>
          </div>
          <div className="w-full">
            <div className="mb-6">
              <Image
                src={
                  formInputFiles.apresentationPhoto.preview ||
                  "https://placehold.co/400x200.svg"
                }
                width={100}
                height={90}
                alt="Apresentation Photo"
                className="rounded-lg w-full h-[200px] object-scale-down"
              />
              <label htmlFor="apresentationPhoto">Foto de apresentação:</label>
              <input
                type="file"
                name="apresentationPhoto"
                id="apresentationPhoto"
                className="pl-[8px] py-[6px]"
                onChange={handleImageChange}
                required
              />
            </div>
            <div className="mb-6">
              <Image
                src={
                  formInputFiles.lateralPhoto.preview ||
                  "https://placehold.co/400x200.svg"
                }
                width={100}
                height={90}
                alt="Lateral Photo"
                className="rounded-lg w-full h-[200px] object-scale-down"
              />
              <label htmlFor="lateralPhoto">Foto lateral:</label>
              <input
                type="file"
                name="lateralPhoto"
                id="lateralPhoto"
                className="pl-[8px] py-[6px]"
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
