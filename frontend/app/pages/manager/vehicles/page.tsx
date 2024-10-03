import TableContainer from "@components/shared/TableContainer";

export default function ManagerVehicles()
{
    return(
        <>
            <TableContainer keys={['modelo', 'marca', 'categoria', 'preço por dia', 'quantidade em estoque', 'ações']} content={['']}/>
        </>
    )
}