import axios from 'axios';

const baseURL = 'http://localhost:8000';

export const getLegislatorsBills = async () => {
    const url = `${baseURL}/legislator/list-bills`;
    return await axios.get(url);
}

export const getBillsDetails = async () => {
    const url = `${baseURL}/bill/list`;
    return await axios.get(url);
}