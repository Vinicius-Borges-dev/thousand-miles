import { forwardRef } from "react";

const Table = forwardRef<HTMLTableElement, { children: React.ReactNode }>(
  ({ children }, ref) => {
    return (
      <table
        className="w-full h-full border border-red-500 absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 *:font-open-sans"
        ref={ref}
      >
        {children}
      </table>
    );
  }
);

Table.displayName = "Table";

export default Table;
