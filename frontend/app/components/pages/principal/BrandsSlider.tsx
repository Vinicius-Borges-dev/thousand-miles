import fs from "fs";
import Image from "next/image";
import path from "path";

export default function BrandsSlider() {
  const brandsPath: string = path.join(
    process.cwd(),
    "app",
    "assets",
    "brands"
  );
  const brands:string[] = fs.readdirSync(brandsPath);

  return (
    <section>
      <h1 className="text-white text-center font-asap-condensed-semi-bold text-5xl">
        Principais marcas afiliadas
      </h1>
      <section className="mt-12 w-[calc(100% - 400px)] relative h-[100px]">
        {brands.map((brand, index) => {
          return (
            <div
              className="w-[200px] h-[200px] bg-bg-card rounded-lg flex justify-center items-center mr-3 absolute animate-slide select-none"
              key={index}
            >
              <Image
                src={`/assets/brands/${brand}`}
                alt="logo marca"
                width={200}
                height={200}
                draggable="false"
              />
            </div>
          );
        })}
      </section>
    </section>
  );
}
