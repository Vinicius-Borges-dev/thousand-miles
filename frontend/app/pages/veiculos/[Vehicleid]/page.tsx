"use server";

export default async function ReservarVeiculo({params}:{params:{Vehicleid:string}})
{
    return(
        <h1>Reservar veículo {params.Vehicleid}</h1>
    )
}