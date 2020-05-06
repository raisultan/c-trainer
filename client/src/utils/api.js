import axios from 'axios';

// TODO use env
const baseUrl = 'http://localhost:8000/api';

export default {
  getCompressorList: () => axios.get(`${baseUrl}/catalog/`),
  login: (username, password) => axios.post(`${baseUrl}/auth/login`, { username, password }),
}
