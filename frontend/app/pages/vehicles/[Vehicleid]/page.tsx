"use client";

import Image from "next/image";
import bmwCinza from "@images/bmw-cinza.png";
import iconCar from "@icons/iconCar.svg";
import steringWheel from "@icons/stering-wheel.svg";
import seat from "@icons/seat.svg";
import Link from "next/link";
import { useEffect, useRef, useState } from "react";

export default function ReservarVeiculo({
  params,
}: {
  params: { Vehicleid: string };
}) {
  const vehicle = params.Vehicleid;

  const [entry_date, setEntry_date] = useState<Date | null>(null);
  const [end_date, setEnd_date] = useState<Date | null>(null);
  let priceRef = useRef<HTMLDivElement | null>(null);
  let entryFeedbackRef = useRef<HTMLSpanElement | null>(null);
  let endFeedbackRef = useRef<HTMLSpanElement | null>(null);

  useEffect(() => {
    if (entry_date && end_date) {
      let today = new Date().getDay() - 1;
      const entry = entry_date.getDay();
      const end = end_date.getDay();

      if (entry < today) {
        entryFeedbackRef.current.textContent =
          "Data de entrada não pode ser anterior a data de hoje";
      } else if (end < entry) {
        endFeedbackRef.current.textContent =
          "Data de saída não pode ser anterior a data de entrada";
      } else {
        entryFeedbackRef.current.textContent = "";
        endFeedbackRef.current.textContent = "";
        const days = Math.abs(end - entry) + 1;
        const price = days * 100;
        const fixedPrice = price.toFixed(2);
        priceRef.current.textContent = `R$ ${fixedPrice.replace(".", ",")}`;
      }
    }
  }, [entry_date, end_date]);

  return (
    <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full">
      <div className="w-full bg-card-form p-2 rounded-md min-[770px]:flex relative shadow-lg shadow-card-form-lighter">
        <section className="flex flex-col p-4 lg:w-1/2 max-md:w-full *:select-none">
          <span className="flex w-full justify-between">
            <h1 className="text-3xl font-asap-condensed-semibold">
              Veículo reservado
            </h1>
            <span className="text-3xl font-asap-condensed-semibold">
              R$ 100,00
            </span>
          </span>
          <h2 className="text-center text-2xl font-bold tracking-widest">
            BMW
          </h2>
          <Image src={bmwCinza} alt="modelo da marca" className="w-full" />
          <section className="flex w-full justify-between [&>div>span>p]:text-gray-400 [&>div>h3]:text-xl">
            <div>
              <span className="flex gap-2">
                <Image src={iconCar} alt="Icone de tipo de veículo" />
                <p className="text-xl font-semibold">Tipo de veículo</p>
              </span>
              <h3 className="font-semibold">Esportivo</h3>
            </div>
            <div>
              <span className="flex gap-2">
                <Image src={steringWheel} alt="Icone de cambio" />
                <p className="text-xl font-semibold">Cambio</p>
              </span>
              <h3 className="font-semibold">Esportivo</h3>
            </div>
            <div>
              <span className="flex gap-2">
                <Image src={seat} alt="Icone de assento" />
                <p className="text-xl font-semibold">Numero de assentos</p>
              </span>
              <h3 className="font-semibold">Esportivo</h3>
            </div>
          </section>
        </section>
        <span className="w-[4px] h-[calc(100%-1rem)] bg-card-form-lighter absolute top-1/2 left-1/2 -translate-y-1/2 rounded-full max-[770px]:hidden"></span>
        <section className="p-4 lg:w-1/2 max-md:w-full">
          <h3 className="text-center text-3xl font-asap-condensed-semibold">
            Reservar veículo
          </h3>
          <form className="h-full relative">
            <section className="md:flex md:flex-row [&>div>input]:bg-input [&>div>input]:text-dark-font [&>div>input]:font-open-sans-condensed-bold [&>div>label]:font-open-sans-condensed-bold [&>div>label]:mb-2 [&>div>input]:mb-6 [&>div>input]:p-3 [&>div>input]:rounded-md [&>div>input]:outline-blue-400 ">
              <div className="flex flex-col md:w-full lg:w-1/2">
                <label htmlFor="entry_date">Data de entrada:</label>
                <input
                  type="date"
                  id="entry_date"
                  name="entry_date"
                  onChange={(e) => setEntry_date(new Date(e.target.value))}
                  required
                />
                <span ref={entryFeedbackRef} className="text-red-500"></span>
                <label htmlFor="end_date">Data de saída:</label>
                <input
                  type="date"
                  id="end_date"
                  name="end_date"
                  onChange={(e) => setEnd_date(new Date(e.target.value))}
                  required
                />
                <span ref={endFeedbackRef} className="text-red-500"></span>
              </div>
              <div className="md:w-full lg:w-1/2">
                <h3 className="text-center text-xl font-semibold">
                  Valor total
                </h3>
                <h3
                  className="text-center text-5xl font-semibold"
                  ref={priceRef}
                ></h3>
              </div>
            </section>
            <div className="flex gap-3 absolute bottom-[2rem] w-full">
              <button className="max-md:full w-1/2 bg-blue-500 text-white font-asap-condensed-semibold p-4 rounded-md mt-4 uppercase">
                Reservar
              </button>
              <Link
                href={"/pages/vehicles/index"}
                className="max-md:full w-1/2 bg-red-500 text-white font-asap-condensed-semibold p-4 rounded-md mt-4 uppercase text-center"
              >
                Cancelar
              </Link>
            </div>
          </form>
        </section>
      </div>
    </div>
  );
}
