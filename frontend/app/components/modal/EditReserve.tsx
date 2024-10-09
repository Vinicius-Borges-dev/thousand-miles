type EditReserveProps = {
    reserveId: number;
}

export default function EditReserve({ reserveId }: EditReserveProps) {
    return (
        <>
            <h1>{reserveId}</h1>
        </>
    )
}