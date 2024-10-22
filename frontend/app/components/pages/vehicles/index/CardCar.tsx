import Image from "next/image";
import steringWheel from "@icons/stering-wheel.svg";
import seat from "@icons/seat.svg";
import Link from "next/link";

type CardCarsProps = {
  id: number;
  model: string;
  price: number;
  transmission: string;
  seats: number;
  lateral_photo: string;
}

export default function CardCars({id, model, price, transmission, seats, lateral_photo}:CardCarsProps) {
  price = (price.toFixed(2)).replace(".", ","); 
  lateral_photo = lateral_photo.replace("\\", "/");
  return (
    <div className="w-[350px] bg-card-cars rounded-lg shadow-md shadow-slate-50 relative flex flex-col items-center justify-between">
      <div className="w-full flex justify-between p-3">
        <h1 className="text-2xl font-alumni text-slate-600">{model}</h1>
        <h2 className="font-open-sans text-slate-700 text-3xl font-semibold">
          R${price}<span className="text-slate-400">/dia</span>
        </h2>
      </div>
      <Image className="p-3" src={`/api/${lateral_photo}`} width={500} height={500} alt="Bmw Cinza" />
      <div className="w-full flex justify-between p-3 *:text-slate-700 *:font-open-sans *:font-semibold">
        <span className="flex gap-2">
          <Image src={steringWheel} alt="icone volante" />
          <p>{transmission}</p>
        </span>
        <span className="flex gap-2">
          <Image src={seat} alt="icone assento" />
          <p>{seats} lugares</p>
        </span>
      </div>
      <Link
        href={`${id}`}
        className="w-[calc(100%-(.75rem*2))] p-4 bg-blue-400 text-white rounded-lg mb-3 text-center font-semibold uppercase tracking-widest"
      >
        Alugar veículo
      </Link>
    </div>
  );
}
