"use server";

import Image from "next/image";
import BmwCinza from "@images/bmw-cinza.png";
import steringWheel from "@icons/stering-wheel.svg";
import seat from "@icons/seat.svg";
import Link from "next/link";

export default async function CardCars() {
  /* const test = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api`);
  
  console.log(test.json()); */

  return (
    <div className="w-[350px] bg-card-cars rounded-lg shadow-md shadow-slate-50 relative flex flex-col items-center">
      <div className="w-full flex justify-between p-3">
        <h1 className="text-2xl font-alumni text-slate-600">BWM</h1>
        <h2 className="font-open-sans text-slate-700 text-3xl font-semibold">
          R$80,00 <span className="text-slate-400">/dia</span>
        </h2>
      </div>
      <Image className="p-3" src={BmwCinza} alt="Bmw Cinza" />
      <div className="w-full flex justify-between p-3 *:text-slate-700 *:font-open-sans *:font-semibold">
        <span className="flex gap-2">
          <Image src={steringWheel} alt="icone volante" />
          <p>Automático</p>
        </span>
        <span className="flex gap-2">
          <Image src={seat} alt="icone assento" />
          <p>2 lugares</p>
        </span>
      </div>
      <Link
        href={`/pages/vehicles/1`}
        className="w-[calc(100%-(.75rem*2))] p-4 bg-blue-400 text-white rounded-lg mb-3 text-center font-semibold uppercase tracking-widest"
      >
        Alugar veículo
      </Link>
    </div>
  );
}
