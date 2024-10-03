import CardCars from "./CardCar";

export default function GridCars() {
  return (
    <section className="grid grid-cols-4 gap-4 mt-20">
        {Array.from({ length: 16 }).map((_, index) => (
            <CardCars key={index} />
        ))}
    </section>
  );
}
