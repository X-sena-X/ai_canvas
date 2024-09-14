const { Variable } = require("lucide-react");

module.exports = {
    plugins: {
        "postcss-present-mantine": {},
        "postcss-simple-vars": {
            Variables: {
                "mantime-breakpoint-xs": "36em",
                "mantime-breakpoint-sm": "48em",
                "mantime-breakpoint-md": "62em",
                "mantime-breakpoint-lg": "75em",
                "mantime-breakpoint-xl": "88em",
            },
        },
    },
};
