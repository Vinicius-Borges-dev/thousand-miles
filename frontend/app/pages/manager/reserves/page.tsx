import searchIcon from "@icons/searchIcon.svg";
import Image from "next/image";

export default function HeaderMyReserves() {
  return (
    <>
      <header>
        <section className="flex flex-col items-center mt-12">
          <h1 className="text-white text-3xl font-open-sans text-center mb-5">
            Busque pela sua reserva ou veja todas listadas abaixo
          </h1>
          <form className="bg-slate-400 w-[500px] p-2 rounded-full flex gap-1">
            <input type="text" className="w-[90%] rounded-full bg-transparent outline-none text-xl text-gray-200 placeholder:text-gray-200 pl-2" placeholder="EX.Bmw"/>
            <select name="filter" id="filter" className="text-gray-300 bg-slate-500 rounded-full px-4 *:font-bold outline-none tracking-widest uppercase [&>options]:p-2" defaultValue={"DEFAULT"}>
                <option value="DEFAULT">filtro</option>
                <option value="all">Todos</option>
                <option value="modelo">Modelo</option>
                <option value="marca">Marca</option>
            </select>
            <button
              className="bg-blue-400 rounded-full w-[60px] h-[50px] flex justify-center items-center"
              type="submit"
            >
              <Image src={searchIcon} alt="icone de pesquisa" />
            </button>
          </form>
        </section>
      </header>
    </>
  );
}
