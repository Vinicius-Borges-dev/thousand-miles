"use server";

export const addNewUser = async (formContent: FormData) => {
    try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/users/register`, {
            method: "POST",
            body: formContent,
        });
        const data = await response.json();
        return data;
    } catch (err) {
        throw new Error("Erro na requisição: " + err);
    }
}

export const login = async(formContent: FormData) => {
    try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/users/login`,{
            method: "POST",
            body: formContent,
        })

        const data = await response.json()

        return data
    } catch (err) {
        throw new Error("Erro na requisição:" + err)
    }
}