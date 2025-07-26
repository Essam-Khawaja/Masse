module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',    // <-- This is crucial for App Router
    './components/**/*.{js,ts,jsx,tsx}',
    // './pages/**/*.{js,ts,jsx,tsx}', // You can keep or remove pages if you don't use it
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};