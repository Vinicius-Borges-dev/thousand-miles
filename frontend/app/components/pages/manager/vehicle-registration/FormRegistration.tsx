"use client";

import Image from "next/image";
import { useEffect, useState } from "react";

export default function FormRegistration() {
  const [FormValues, setFormValues] = useState({
    brand: "",
    model: "",
    category: "",
    year: "",
    color: "",
    pricePerDay: "",
    ApresentationPhoto: "",
    lateralPhoto: "",
  });
  const [error, setError] = useState<string>("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormValues({
      ...FormValues,
      [e.target.name]: e.target.value,
    });
  };

  const validateForm = () => {
    if (
      FormValues.brand === "" ||
      FormValues.model === "" ||
      FormValues.category === "" ||
      FormValues.year === "" ||
      FormValues.color === "" ||
      FormValues.pricePerDay === ""
    ) {
      setError("Preencha todos os campos!");
      return false;
    }
  };

  const submitForm = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (validateForm()) {
      console.log(FormValues);
    }
  };

  const onImageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setFormValues({
          ...FormValues,
          [event.target.name]: e.target.result,
        });
      };
      reader.readAsDataURL(event.target.files[0]);
    }
  };

  return (
    <div className="bg-card-form p-3 rounded-md">
      <h1 className="text-2xl font-open-sans text-center">
        Registro de novo veiculo
      </h1>
      <form onSubmit={submitForm}>
        <div className="lg:flex">
          <div className="w-full px-2 [&>div>input]:w-full [&>div>input]:bg-input [&>div>input]:rounded-lg">
            <div className="mb-6">
              <label htmlFor="brand">Marca do veículo:</label>
              <input
                type="text"
                name="brand"
                id="brand"
                placeholder="Ex.BMW"
                className="pl-[8px] py-[6px]"
                onChange={handleChange}
                required
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
                onChange={handleChange}
                required
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
                onChange={handleChange}
                required
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
                onChange={handleChange}
                required
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
                onChange={handleChange}
                required
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
                onChange={handleChange}
                required
              />
            </div>
          </div>
          <div className="w-full">
            <div className="mb-6">
              <Image
                src={
                  FormValues.ApresentationPhoto ||
                  "https://placehold.co/400x200.svg"
                }
                width={100}
                height={90}
                alt="Apresentation Photo"
                className="rounded-lg w-full h-[200px] object-scale-down"
              />
              <label htmlFor="ApresentationPhoto">Foto de apresentação:</label>
              <input
                type="file"
                name="ApresentationPhoto"
                id="ApresentationPhoto"
                className="pl-[8px] py-[6px]"
                onChange={onImageChange}
              />
            </div>
            <div className="mb-6">
              <Image
                src={
                  FormValues.lateralPhoto ||
                  "https://placehold.co/400x200.svg"
                }
                width={100}
                height={90}
                alt="Apresentation Photo"
                className="rounded-lg w-full h-[200px] object-scale-down"
              />
              <label htmlFor="lateralPhoto">Foto lateral:</label>
              <input
                type="file"
                name="lateralPhoto"
                id="lateralPhoto"
                className="pl-[8px] py-[6px]"
                onChange={onImageChange}
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
