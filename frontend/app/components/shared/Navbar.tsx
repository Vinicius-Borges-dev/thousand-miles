import Link from "next/link";

export default function Navbar() {
  return (
    <header className="p-4 fixed w-full top-0 z-10">
      <nav className="w-full bg-opacity-50 bg-gray-950 p-2 flex justify-center border-b-4 border-gray-500">
        <ul className="flex gap-8 *:font-open-sans-condensed-light">
          <li className="text-3xl p-2">
            <Link
              className="text-gray-300 hover:text-gray-500 transition-all"
              href="#"
            >
              Carros disponíveis
            </Link>
          </li>
          <li className="text-3xl p-2">
            <Link
              className="text-gray-300 hover:text-gray-500 transition-all"
              href="#"
            >
              Home
            </Link>
          </li>
          <li className="text-3xl p-2">
            <Link
              className="text-gray-300 hover:text-gray-500 transition-all"
              href="#"
            >
              Minhas reservas
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}
