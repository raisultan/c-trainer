import axios from 'axios';

// TODO use env
const baseUrl = 'http://localhost:8000';

const config = {
  headers: {
    Authorization: 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg5MTY4NDUyLCJqdGkiOiI0YjY2ZGUzNjNjNjY0ZmMxYTMzODBjNmMyZWNmZGU3ZiIsInVzZXJfaWQiOjF9.5qi8LT4B7dtTB5wHef0huLEBaB6U4MrgRFn65-vL3Vg'
  }
}
export default {
  baseUrl,
  getCompressorList: () => axios.get(`${baseUrl}/api/catalog/`, config),
  getCompressorPage: (id) => axios.get(`${baseUrl}/api/catalog/${id}`, config),
  login: (username, password) => axios.post(`${baseUrl}/api/auth/login`, { username, password }),
}
