import axios from 'axios'

export const serverAddress = process.env.REACT_APP_SERVER_ADDRESS

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export function login(credentials) {
    return axios.post(serverAddress + '/login/', credentials, {withCredentials: true})
}

export function getTasks() {
    return axios.get(serverAddress + '/task/', {withCredentials: true})
}

export function createTask(data) {
    return axios.post(serverAddress + '/task/', data, {withCredentials: true})
}

export function markTaskDone(id) {
    return axios.patch(serverAddress + '/task/' + id + '/',{}, {withCredentials: true})
}

export function editTask(id, data) {
    return axios.put(serverAddress + '/task/' + id + '/', data, {withCredentials: true})
}

export function deleteTask(id) {
    return axios.delete(serverAddress + '/task/' + id + '/', {withCredentials: true})
}
