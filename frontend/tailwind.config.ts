import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily:{
        "alumni": ["Alumni Sans SemiBold", "sans-serif"],
        "asap-condensed-medium": ["Asap Condensed Medium", "sans-serif"],
        "asap-condensed-regular": ["Asap Condensed Regular", "sans-serif"],
        "asap-condensed-semibold": ["Asap Condensed SemiBold", "sans-serif"],
        "barlow-condensed-bold": ["Asap Condensed Bold", "sans-serif"],
        "barlow-condensed-extra-light": ["Asap Condensed ExtraLight", "sans-serif"],
        "barlow-condensed-medium": ["Asap Condensed Medium", "sans-serif"],
        "barlow-condensed-semibold": ["Asap Condensed SemiBold", "sans-serif"],
        "open-sans-italic": ["Open Sans Italic", "sans-serif"],
        "open-sans": ["OpenSans", "sans-serif"],
        "open-sans-condensed-bold": ["Opensans Condensed Bold", "sans-serif"],
        "open-sans-condensed-light": ["Opensans Condensed Light", "sans-serif"],
      },
      colors:{
        "card": "#f2f2f2",
      },
      animation:{
        "slide": "slider 40s linear infinite",
      },
      }
    },
  },
  plugins: [],
};
export default config;
