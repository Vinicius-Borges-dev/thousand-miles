import Input from "./Input";
import iconEmail from "@icons/iconEmail.svg";
import iconPassword from "@icons/iconLock.svg";
import iconId from "@icons/iconId.svg";
import iconCalendar from "@icons/iconCalendar.svg";
import iconFingerPrint from "@icons/iconFingerprint.svg";
import { useEffect, useRef, useState } from "react";

export default function Account() {
  const [logIn, setLogIn] = useState({
    email: "",
    password: "",
  });

  const [signUp, setSignUp] = useState({
    name: "",
    email: "",
    birthdate: "",
    rg: "",
    cpf: "",
    password: "",
    confirmPassword: "",
  });

  const loginFormRef = useRef<HTMLDivElement | null>(null);
  const signUpFormRef = useRef<HTMLDivElement | null>(null);
  const changeFormToLoginRef = useRef<HTMLButtonElement | null>(null);
  const changeFormToSignUpRef = useRef<HTMLButtonElement | null>(null);

  const handleLogIn = (e: React.ChangeEvent<HTMLInputElement>) => {
    setLogIn({
      ...logIn,
      [e.target.name]: e.target.value,
    });
  };

  const handleSignUp = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSignUp({
      ...signUp,
      [e.target.name]: e.target.value,
    });
  };

  const handleLogInSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log(logIn);
  };

  const handleSignUpSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log(signUp);
  };

  useEffect(() => {
    changeFormToLoginRef.current?.addEventListener("click", () => {
      loginFormRef.current?.classList.remove("hidden");
      signUpFormRef.current?.classList.add("hidden");
    });
    changeFormToSignUpRef.current?.addEventListener("click", () => {
      loginFormRef.current?.classList.add("hidden");
      signUpFormRef.current?.classList.remove("hidden");
    });
  });
  return (
    <section className="flex w-full">
      <div ref={loginFormRef} className="w-full">
        <h1 className="text-2xl font-semibold text-center">
          Entre na sua conta
        </h1>
        <form action="#" className="mb-3" onSubmit={handleLogInSubmit}>
          <Input
            label="Digite seu email:"
            type="email"
            name="email"
            placeholder="Ex. JohnDoe@email.com"
            onChange={handleLogIn}
            icon={iconEmail}
          />
          <Input
            label="Digite sua senha:"
            type="password"
            name="login_password"
            placeholder="********"
            onChange={handleLogIn}
            icon={iconPassword}
          />
          <button className="w-full bg-blue-400 text-white rounded-lg font-semibold py-2 mt-5">
            Entrar
          </button>
        </form>
        <p className="text-center">
          Não possue uma conta?
          <button className="text-blue-400" ref={changeFormToSignUpRef}>
            Cadastre-se
          </button>
        </p>
      </div>
      <div className="hidden w-full" ref={signUpFormRef}>
        <h1 className="text-2xl font-semibold text-center">Cadastre-se</h1>
        <form action="#" className="mb-3" onSubmit={handleSignUpSubmit}>
          <span className="lg:flex lg:gap-10">
            <div className="lg:w-1/2 w-full">
              <Input
                label="Digite seu nome completo:"
                type="text"
                name="username"
                placeholder="Ex. John Doe"
                onChange={handleSignUp}
                icon={iconEmail}
              />
              <Input
                label="Digite seu email:"
                type="email"
                name="signup_email"
                placeholder="Ex. JohnDoe@email.com"
                onChange={handleSignUp}
                icon={iconEmail}
              />
              <Input
                label="Digite sua data de nascimento:"
                type="date"
                name="birthdate"
                onChange={handleSignUp}
                icon={iconCalendar}
              />
              <Input
                label="Digite seu rg:"
                type="text"
                name="rg"
                placeholder="Ex. 123456789"
                onChange={handleSignUp}
                icon={iconId}
              />
            </div>
            <div className="lg:w-1/2 w-full">
              <Input
                label="Digite seu CPF:"
                type="text"
                name="cpf"
                placeholder="Ex. 12345678901"
                onChange={handleSignUp}
                icon={iconFingerPrint}
              />
              <Input
                label="Digite sua senha:"
                type="password"
                name="signup_password"
                placeholder="********"
                onChange={handleSignUp}
                icon={iconPassword}
              />
              <Input
                label="Confirme sua senha:"
                type="password"
                name="signup_confirm_password"
                placeholder="********"
                onChange={handleSignUp}
                icon={iconPassword}
              />
            </div>
          </span>
          <div className="w-full">
            <button className="w-full bg-blue-400 text-white rounded-lg font-semibold py-2">
              Cadastrar
            </button>
          </div>
        </form>
        <p className="text-center">
          Não possue uma conta?
          <button className="text-blue-400" ref={changeFormToLoginRef}>
            Cadastre-se
          </button>
        </p>
      </div>
    </section>
  );
}
