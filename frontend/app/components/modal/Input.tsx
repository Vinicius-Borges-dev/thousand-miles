import Image from "next/image";

type InputProps = {
  label: string;
  type: string;
  name?: string;
  placeholder?: string;
  onChange?: (
    e: React.ChangeEvent<
      HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement
    >
  ) => void;
  feedback?: string;
  icon?: string;
  iconAlt?: string;
  value?: string | number | Date | undefined;
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
  value,
}: InputProps) {
  const iconName = icon?.src.split("/")[4].split(".")[0];

  const InputContructor = (): React.ReactNode => {
    if (type === "textarea") {
      return (
        <textarea
          name={name}
          id={name}
          className="w-full h-[40px] p-2 bg-input outline-none focus:border focus:border-blue-400 font-semibold rounded-lg"
          placeholder={placeholder}
          onChange={onChange}
          value={value}
        ></textarea>
      );
    } else if (type === "submit") {
      return (
        <button
          type="submit"
          className="w-full h-[40px] p-2 bg-blue-400 text-white font-semibold rounded-lg"
        >
          {label}
        </button>
      );
    } else {
      return (
        <input
          type={type}
          name={name}
          id={name}
          placeholder={placeholder}
          onChange={onChange}
          className={`w-full h-[40px] p-2 bg-input ${
            icon ? "rounded-tl-lg rounded-bl-lg" : "rounded-lg"
          } outline-none focus:border focus:border-blue-400 font-semibold`}
          value={value}
          required
        />
      );
    }
  };

  const labelContructor = (): React.ReactNode => {
    if (type === "submit") {
      return "";
    } else {
      return (
        <label htmlFor={name} className="font-bold tracking-wide text-nowrap">
          {label}
        </label>
      );
    }
  };
  return (
    <div className="mb-5 *:font-open-sans first:mt-5">
      {labelContructor()}
      <span className="flex items-center mt-2">
        {InputContructor()}
        {icon && icon !== "" ? (
          <span className="w-[40px] h-[40px] flex justify-center items-center bg-blue-400 rounded-tr-lg rounded-br-lg">
            <Image
              src={icon}
              width={20}
              height={20}
              alt={`${iconAlt}`}
              className={iconName === "iconCar" ? "" : "invert"}
            />
          </span>
        ) : (
          ""
        )}
      </span>
      <span className="text-red-600">{feedback}</span>
    </div>
  );
}
