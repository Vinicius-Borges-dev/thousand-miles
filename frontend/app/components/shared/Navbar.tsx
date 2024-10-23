import Link from "next/link";
import Account from "@components/modal/Account";
import { useModal } from "@root/app/components/modal/BaseModal/ModalContext";
import { useEffect, useState } from "react";

export default function Navbar() {
  const { openModal } = useModal();
  const [logged, setLogged] = useState<boolean>(false);
  const [name, setName] = useState<string | null>(null);

  const killLogin = () => {
    localStorage.clear();
    setLogged(false);
    setName(null);
  };

  useEffect(() => {
    const userName = localStorage.getItem("username");
    if (userName) {
      setLogged(true);
      setName(userName);
    } else {
      setLogged(false);
      setName(null);
    }
  }, []);

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
            Olá, {name ? `${name}` : "Visitante"}
          </div>
          <div className="absolute text-right w-full">
            <ul className="w-full p-3 bg-gray-800 rounded-md [&>li]:mb-3">
              {logged ? (
                <li className="last:mb-0">
                  <button
                    className="text-gray-300 hover:text-gray-500 transition-all"
                    onClick={killLogin}
                  >
                    Sair
                  </button>
                </li>
              ) : (
                <li>
                  <button
                    className="text-gray-300 hover:text-gray-500 transition-all"
                    onClick={() => openModal(<Account />)}
                  >
                    Login
                  </button>
                </li>
              )}
            </ul>
          </div>
        </span>
      </nav>
    </header>
  );
}
