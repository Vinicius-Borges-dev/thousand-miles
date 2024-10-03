import Image from "next/image";
import Logo from "@images/logo.svg";
import { forwardRef } from "react";

const Footer = forwardRef<HTMLDivElement>((props, ref) => {
  return (
    <footer className="w-full mt-40 flex justify-center pb-2 absolute bottom-[-164px]" ref={ref}>
      <ul className="flex gap-4 *:text-white font-open-sans text-2xl items-end">
        <li>Todos os direitos reservados</li>
        <li>
          <Image src={Logo} alt="Logotipo Thousand-Miles" />
        </li>
        <li>2024</li>
      </ul>
    </footer>
  );
});

Footer.displayName = "Footer";

export default Footer;
