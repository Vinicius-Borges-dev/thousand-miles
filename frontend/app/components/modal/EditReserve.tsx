import { useState } from "react";
import Input from "./Input";
import iconUser from "@icons/iconUser.svg";
import iconCar from "@icons/iconCar.svg";
import iconCalendar from "@icons/iconCalendar.svg";

type EditReserveProps = {
  reserveId: number;
};

const DescriptionStatus = () => {
  return (
    <div>
      <textarea
        name="decription_status"
        id="decription_status"
        placeholder="Descreva o motivo do status"
        className="bg-input p-3 outline-none rounded-lg *:font-semibold placeholder:font-semibold mt-3 w-full"
      ></textarea>
    </div>
  );
};

export default function EditReserve({ reserveId }: EditReserveProps) {
  const [UpdateFormData, setUpdateFormData] = useState({
    id: reserveId,
    client: "John Doe",
    car: "I8",
    entry_data: new Date("10/01/2024").toISOString().split("T")[0],
    end_data: new Date("10/05/2024").toISOString().split("T")[0],
    status: "pendente",
  });

  const handleFillForm = (
    event: React.ChangeEvent<HTMLInputElement & HTMLSelectElement>
  ) => {
    setUpdateFormData({
      ...UpdateFormData,
      [event.target.name]: event.target.value,
    });
    console.log(UpdateFormData);
  };

  return (
    <form>
      <div>
        <Input
          label="Cliente:"
          type="text"
          name="client"
          onChange={handleFillForm}
          icon={iconUser}
          value={UpdateFormData.client}
        />
        <Input
          label="Veículo:"
          type="text"
          name="car"
          onChange={handleFillForm}
          icon={iconCar}
          value={UpdateFormData.car}
        />
        <Input
          label="Data de entrada:"
          type="date"
          name="entry_data"
          onChange={handleFillForm}
          icon={iconCalendar}
          value={UpdateFormData.entry_data}
        />
        <Input
          label="Data de saída:"
          type="date"
          name="end_data"
          onChange={handleFillForm}
          icon={iconCalendar}
          value={UpdateFormData.end_data}
        />
        <h2 className="text-2xl mb-3">Gerenciar status</h2>
        <select
          name="status"
          id="status"
          className="bg-input p-3 outline-none rounded-lg *:font-semibold"
          onChange={handleFillForm}
          defaultValue={UpdateFormData.status}
        >
          <option value="ativo">Ativo</option>
          <option value="pendente">
            Pendente
          </option>
          <option value="cancelado">Cancelado</option>
        </select>

        {UpdateFormData.status === "cancelado" ? <DescriptionStatus /> : ""}
        <input type="submit" value="Enviar" className="bg-blue-500 mt-4 w-full p-3 rounded-lg text-xl font-semibold"/>
      </div>
    </form>
  );
}
