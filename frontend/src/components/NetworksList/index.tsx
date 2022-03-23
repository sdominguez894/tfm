import React, { useContext } from "react";
import { useQuery } from "react-query";
import { AppContext } from "../../contexts/appContext";
import { FetchService } from "../../services/fetchService";


const NetworksList = () => {

  const { blockchain, setBlockchain } = useContext(AppContext);
  const { isLoading, error, data } = useQuery("blockchains", 
                                              () => FetchService.fetch("blockchains"));

  if (isLoading) return <div>Loading...</div>; //TODO - Loading component

  if (error) return <div>An error has occurred</div>; //TODO - Error component

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
