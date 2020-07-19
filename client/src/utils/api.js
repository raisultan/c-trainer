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
  // training lesson
  getTrainings: () => axios.get(`${baseUrl}/api/catalog/`, getConfig()),
  submitTrainingAnswer: () => axios.get(`${baseUrl}/api/catalog/`, getConfig()),
  getTrainingResult: () => axios.get(`${baseUrl}/api/catalog/`, getConfig()),
  // exam
  getExams: () => axios.get(`${baseUrl}/api/catalog/`, getConfig()),
  startExam: () => axios.get(`${baseUrl}/api/catalog/`, getConfig()),
  finishExam: () => axios.get(`${baseUrl}/api/catalog/`, getConfig()),
}
