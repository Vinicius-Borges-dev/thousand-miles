import Image from "next/image";
import SearchIcon from "@icons/searchIcon.svg";
import Link from "next/link";

export default function Header() {
  return (
    <header className="w-full flex justify-center items-center xl:h-[700px] lg:h-[300px]">
      <section className="*:text-white">
        <h1 className="xl:text-6xl lg:text-4xl font-asap-condensed-medium text-center mb-5">
          A um clique de alugar o luxo sobre rodas
        </h1>
        <p className="text-2xl font-asap-condensed-regular text-center mb-5">
          Veja todos os veículos disponiveis para você.
        </p>
        <div className="bg-slate-200 py-3 px-3 w-2/3 rounded-full mx-auto">
          <Link href="/veiculos" className="w-full flex justify-between">
            <button
              type="submit"
              className="text-slate-400 font-asap-condensed-semi-bold"
            >
              Ver todos os veículos
            </button>
            <Image
              src={SearchIcon}
              className="bg-blue-500 p-6 rounded-full"
              alt="botão de pesquisa"
            />
          </Link>
        </div>
      </section>
    </header>
  );
}
