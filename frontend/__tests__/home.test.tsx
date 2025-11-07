import { render, screen } from "@testing-library/react";

import HomePage from "../app/page";

describe("HomePage", () => {
  it("renders dashboard sections", () => {
    render(<HomePage />);

    expect(screen.getByText(/Welcome back/i)).toBeInTheDocument();
    expect(screen.getByText(/Sales Pipeline/i)).toBeInTheDocument();
    expect(screen.getByText(/Recent Activities/i)).toBeInTheDocument();
    expect(screen.getByText(/Upcoming Tasks/i)).toBeInTheDocument();
  });
});
