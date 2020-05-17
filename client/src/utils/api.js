import axios from 'axios';
import authProvider from "../auth/authProvider";

// TODO use env
const baseUrl = 'http://localhost:8000';

const getConfig = () => ({
  headers: { Authorization: `Bearer ${authProvider.getAccessToken()}` }
})

export default {
  baseUrl,
  getCompressorList: () => axios.get(`${baseUrl}/api/catalog/`, getConfig()),
  getCompressorPage: (id) => axios.get(`${baseUrl}/api/catalog/${id}`, getConfig()),
  login: (username, password) => axios.post(`${baseUrl}/api/auth/login/`, { username, password }),
}
