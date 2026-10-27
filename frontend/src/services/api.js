import axios from "axios";


const api = axios.create({
  baseURL:
    "http://127.0.0.1:8000/api",

  timeout: 10000,
});


export async function getDashboard() {

  const response =
    await api.get(
      "/dashboard/"
    );

  return response.data;
}


export async function getGraph() {

  const response =
    await api.get(
      "/graph/"
    );

  return response.data;
}


export async function getEntities() {

  const response =
    await api.get(
      "/entities/"
    );

  return response.data;
}


export async function getAnomalies() {

  const response =
    await api.get(
      "/anomalies/"
    );

  return response.data;
}


export async function generateEvents(
  count = 100
) {

  const response =
    await api.post(
      `/simulation/generate?count=${count}`
    );

  return response.data;
}


export default api;