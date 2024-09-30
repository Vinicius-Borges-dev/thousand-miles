import Image from "next/image";
import ImagemTopo from "@images/topo.svg";
import ImagemBaixo from "@images/base.svg";
import { forwardRef } from "react";

const Background = forwardRef<HTMLDivElement>((props, ref) => {
    return(
      <div className="w-full absolute">
      <section className="w-full relative" ref={ref}>
        <Image className="w-full" src={ImagemTopo} alt="Imagem do topo" />

        <Image
          className="w-full absolute bottom-0 z-[-2]"
          src={ImagemBaixo}
          alt="Imagem de baixo"
        />
      </section>
    </div>
    )
});

Background.displayName = "Background";

export default Background;