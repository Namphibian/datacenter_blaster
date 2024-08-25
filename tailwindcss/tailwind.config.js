/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: 'class',
    content: [
        "../src/static/**/*.{html,js}",
        "../src/templates/**/*.{html,js}",
        'node_modules/preline/dist/*.js',
    ],
    theme: {
        extend: {
            // extend base Tailwind CSS utility classes
        },
    },
    plugins: [
        require("@tailwindcss/typography"),
        require("@tailwindcss/forms"),
        require("preline/plugin")
    ],
};