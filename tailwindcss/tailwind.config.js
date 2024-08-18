/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "../src/static/**/*.{html,js}",
        "../src/templates/**/*.{html,js}",
        "node_modules/daisyui/dist/full.css",
        "node_modules/flowbite/**/*.js"
    ],
    theme: {
        extend: {},
    },
    daisyui: {
        themes: false,
    },
    plugins: [
        require("daisyui"),
        require('flowbite/plugin')({
            datatables: true,
            charts: true,
            forms: true,
            tooltips: true
        }),
    ],
};