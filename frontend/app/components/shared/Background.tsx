import Image from "next/image";
import ImagemTopo from "@images/topo.svg";
import ImagemBaixo from "@images/base.svg";

export default function Background() {
  return (
    <span className="w-full absolute">
      <section className="w-full relative" id="global">
        <Image className="w-full" src={ImagemTopo} alt="Imagem do topo" />

        <Image
          className="w-full absolute bottom-0 z-[-2]"
          src={ImagemBaixo}
          alt="Imagem de baixo"
        />
      </section>
    </span>
  );
}
