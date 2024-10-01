import Image from "next/image";
import brands from "@brands/__brandsMock";

export default function BrandsSlider() {
  return (
    <section>
      <h1 className="text-white text-center font-asap-condensed-semi-bold text-5xl">
        Principais marcas afiliadas
      </h1>
      <section className="mt-12 w-[calc(100% - 400px)] relative h-[100px]">
        {brands.map((brand, index) => (
          <div
            className="w-[200px] h-[200px] bg-card rounded-lg flex justify-center items-center mr-3 absolute animate-slide select-none left-[200%]"
            key={index}
          >
            <Image
              src={brand}
              alt={`Brand ${index + 1}`}
            />
          </div>
        ))}
      </section>
    </section>
  );
}
