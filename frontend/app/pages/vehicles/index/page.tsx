import Header from "@root/app/components/pages/vehicles/index/Header";
import GridCars from "@root/app/components/pages/vehicles/index/GridCars";
import { forwardRef } from "react";

const Veiculos = forwardRef<HTMLDivElement>((props, ref) => {
    return(
        <div ref={ref}>
            <Header />
            <GridCars/>
        </div>
    )
})

Veiculos.displayName = "Veiculos";

export default Veiculos;