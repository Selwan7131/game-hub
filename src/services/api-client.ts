import axios from "axios";

// costume configuration
// with this configuration the key will be included in the query string of every http request sent to the backend
export default axios.create({
  baseURL: "https://api.rawg.io/api",
  params: {
    key: "7258df424a7c4b2f8ddaf5fd3836b4ee",
  },
});
