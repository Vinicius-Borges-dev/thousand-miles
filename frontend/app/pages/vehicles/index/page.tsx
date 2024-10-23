"use client";

import GridCars from "@root/app/components/pages/vehicles/index/GridCars";
import Image from "next/image";
import searchIcon from "@icons/searchIcon.svg";
import { createContext, useState } from "react";

export const VeiculosContext = createContext<string | null>(null);

export default function VeiculosProvider () {
  const [search, setSearch] = useState<string>("");

  return (
    <VeiculosContext.Provider value={search}>
      <header>
        <section className="flex flex-col items-center mt-12">
          <h1 className="text-white text-3xl font-open-sans text-center mb-5">
            Busque pelo veículo ou veja todos listados abaixo
          </h1>
          <form className="bg-slate-400 w-[500px] p-2 rounded-full flex justify-between">
            <input
              className="w-full p-2 text-2xl text-slate-700 bg-transparent rounded-full focus:outline-none"
              type="search"
              name="search_car"
              id="search_car"
              placeholder="Ex.Bmw"
              onChange={(e) => setSearch(e.target.value)}
            />
            <button
              className="bg-blue-400 rounded-full w-[60px] h-[50px] flex justify-center items-center"
              type="submit"
            >
              <Image src={searchIcon} alt="icone de pesquisa" />
            </button>
          </form>
        </section>
      </header>
      <GridCars />
    </VeiculosContext.Provider>
  );
};
