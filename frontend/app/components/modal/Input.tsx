import Image from "next/image";

type InputProps = {
  label: string;
  type: string;
  name: string;
  placeholder?: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  feedback?: string;
  icon?: string;
  iconAlt?: string;
};

export default function Input({
  label,
  type,
  name,
  placeholder,
  onChange,
  feedback,
  icon,
  iconAlt,
}: InputProps) {
  return (
    <div className="mb-5 *:font-open-sans first:mt-5">
      <label htmlFor={name} className="font-bold tracking-wide text-nowrap">
        {label}
      </label>
      <span className="flex items-center mt-2">
        <input
          type={type}
          name={name}
          id={name}
          placeholder={placeholder}
          onChange={onChange}
          className="w-full h-[40px] p-2 bg-input rounded-tl-lg rounded-bl-lg outline-none focus:border focus:border-blue-400 font-semibold"
          required
        />
        {icon && icon !== "" ? (
          <span className="w-[40px] h-[40px] flex justify-center items-center bg-blue-400 rounded-tr-lg rounded-br-lg">
            <Image src={icon} width={20} height={20} alt={`${iconAlt}`} className="invert"/>
          </span>
        ) : (
          ""
        )}
      </span>
      <span className="text-red-600">{feedback}</span>
    </div>
  );
}
