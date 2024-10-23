"use server";
import jwt from "jsonwebtoken";

export const addNewUser = async (formContent: FormData) => {
  try {
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/users/register`,
      {
        method: "POST",
        body: formContent,
      }
    );
    const data: { status: string; message: string } = await response.json();
    return data;
  } catch (err) {
    throw new Error("Erro na requisição: " + err);
  }
};

export const login = async (formContent: FormData) => {
  try {
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/users/login`,
      {
        method: "POST",
        body: formContent,
      }
    );

    const data: { status: string; message: string; token: string } =
      await response.json();

    return data;
  } catch (err) {
    throw new Error("Erro na requisição:" + err);
  }
};

export const getTokenData = (token: string) => {
  try {
    const tokenData: {
      id: number;
      name: string;
      access_level: string;
      exp: number;
    } = jwt.decode(token);
    return tokenData;
  } catch (err) {
    throw new Error("Erro ao capturar o token: " + err);
  }
};

export const getEmployeePermission = (role:string | null) => {
  if (role !== "employee" || !role) return false;
  return true;
};
