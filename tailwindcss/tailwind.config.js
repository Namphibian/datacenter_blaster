/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme");
const colors = require("tailwindcss/colors");
module.exports = {
    content: [
        "../src/static/**/*.{html,js}",
        "../src/templates/**/*.{html,js}",
        "node_modules/daisyui/dist/full.css",
        "node_modules/flowbite/**/*.js"
    ],
    theme: {
        extend: {
            // Set font family
            fontFamily: {
                sans: ["Inter", ...defaultTheme.fontFamily.sans],
            },
            // Set theme colors (Required config!)
            colors: {
                primary: colors.blue,
                secondary: colors.slate,
            },
        },
    },
    daisyui: {
        themes: false,
    },
    plugins: [
        // require("daisyui"),
          require('flowbite/plugin')({
            datatables: true,
            charts: true,
            forms: true,
            tooltips: true
        }),
        require("@tailwindcss/typography"), require("@tailwindcss/forms")
    ],
};