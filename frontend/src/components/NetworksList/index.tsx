import React, { useContext } from "react";
import { useQuery } from "react-query";
import { AppContext } from "../../contexts/appContext";
import { FetchService } from "../../services/fetchService";
import Error from "../Error";


const NetworksList = () => {

  const { blockchain, setBlockchain } = useContext(AppContext);
  const { isLoading, error, data } = useQuery("blockchains", 
                                              () => FetchService.fetch("blockchains"));

  if (isLoading) return <div></div>; //Loading

  if (error) return <Error/>; //Error

  return (
    <select
      style={{ width: "auto" }}
      className="form-select md-2 m-2"
      aria-label="Networks select"
      onChange={(event) => setBlockchain(event.target.value)}
    >
      {data.map((blockchain: string) => (
        <option key={blockchain} 
                value={blockchain}>
          {blockchain}
        </option>
      ))}
    </select>
  );
};

export default NetworksList;
