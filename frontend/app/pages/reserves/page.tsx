import TableContainer from "@root/app/components/shared/TableContainer";
import HeaderMyReserves from "../manager/reserves/page";

export default function Reserves()
{

    const content: Array<Array<string | number>> = [
        [
            "I8",
            "BMW",
            "Esportivo",
            500.00,
            1500.00,
            "ativo",
            "cancelar"
        ],
        [
            "I8",
            "BMW",
            "Esportivo",
            500.00,
            1500.00,
            "pendente",
            "cancelar"
        ],
        [
            "I8",
            "BMW",
            "Esportivo",
            500.00,
            1500.00,
            "cancelado",
            ""
        ],
    ];
    return (
        <>
            <HeaderMyReserves />
            <TableContainer keys={["Carro","Marca","Tipo","preço por dia","preço total", "status", "Ações"]} content={content}/>
        </>
    )
}
