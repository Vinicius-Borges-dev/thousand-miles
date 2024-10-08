import Link from "next/link";

export default function Navbar() {
  return (
    <header className="p-4 fixed w-full top-0 z-10">
      <nav className="w-full bg-opacity-50 bg-gray-950 p-2 flex justify-between border-b-4 border-gray-500">
        <span>
          <ul className="flex gap-8 *:font-open-sans-condensed-light">
            <li className="text-3xl p-2">
              <Link
                className="text-gray-300 hover:text-gray-500 transition-all"
                href="/"
              >
                Home
              </Link>
            </li>
            <li className="text-3xl p-2">
              <Link
                className="text-gray-300 hover:text-gray-500 transition-all"
                href="/pages/vehicles/index"
              >
                Carros disponíveis
              </Link>
            </li>
            <li className="text-3xl p-2">
              <Link
                className="text-gray-300 hover:text-gray-500 transition-all"
                href="/pages/manager/vehicles"
              >
                Todos os Veículos
              </Link>
            </li>
            <li className="text-3xl p-2">
              <Link
                className="text-gray-300 hover:text-gray-500 transition-all"
                href="/pages/manager/vehicle-registration"
              >
                Cadastrar novo veículo
              </Link>
            </li>
            <li className="text-3xl p-2">
              <Link
                className="text-gray-300 hover:text-gray-500 transition-all"
                href="/pages/reserves"
              >
                Minhas reservas
              </Link>
            </li>
            <li className="text-3xl p-2">
              <Link
                className="text-gray-300 hover:text-gray-500 transition-all"
                href="/pages/manager/reserves"
              >
                Todas as reservas
              </Link>
            </li>
          </ul>
        </span>
        <span className="relative">
          <div className="flex items-center text-2xl">
            Olá, Visitante
          </div>
          <div className="absolute text-right w-full">
              <ul className="w-full p-3 bg-gray-800 rounded-md [&>li]:mb-3">
                <li>
                  <button
                    className="text-gray-300 hover:text-gray-500 transition-all"
                  >
                    Login
                  </button>
                </li>
                <li>
                  <button
                    className="text-gray-300 hover:text-gray-500 transition-all"
                  >
                    Registrar
                  </button>
                </li>
                <hr className="w-full h-[2px] bg-slate-400"/>
                <li className="last:mb-0">
                  <button
                    className="text-gray-300 hover:text-gray-500 transition-all"
                  >
                    Sair
                  </button>
                </li>
              </ul>
          </div>
        </span>
      </nav>
    </header>
  );
}
