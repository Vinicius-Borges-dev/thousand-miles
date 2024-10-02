export default function Table({children}: {children: React.ReactNode})
{
    return(
        <table className="w-full absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 *:font-open-sans">
            {children}
        </table>
    )
}