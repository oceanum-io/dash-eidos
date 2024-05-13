const config = require("./webpack.config.js");
const path = require("path");

config.entry = { main: "./src/demo/index.jsx" };
config.output = {
  filename: "./output.js",
};
config.mode = "development";
config.externals = undefined; // eslint-disable-line
config.devtool = "source-map";

module.exports = config;
