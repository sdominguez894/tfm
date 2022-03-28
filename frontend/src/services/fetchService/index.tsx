import config from "../../config";

export class FetchService {

    static fetch = async (path: string) => {
        const endpoint = `${config.BACKEND_URL}${path}`;
        //console.log(`ENDPOINT: ${endpoint}`);
        const res = await fetch(endpoint);
        const data = await res.json();
        //console.log(`DATA: ${data}`);
        return data;
    };

}