import "@testing-library/jest-dom";

jest.mock("next/navigation", () => ({
  usePathname: () => "/",
  useRouter: () => ({ push: jest.fn(), prefetch: jest.fn() })
}));
