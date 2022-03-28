import React, { useContext } from "react";
import { useQuery } from "react-query";
import { AppContext } from "../../contexts/appContext";
import { FetchService } from "../../services/fetchService";
import Loading from "../Loading";
import Error from "../Error";
import { Block } from "../../Models/Block";
import { Link } from "react-router-dom";


const Blocks = () => {

  const { blockchain, setBlockchain } = useContext(AppContext);
  const { isLoading, error, data } = useQuery("blocks", 
                                              () => FetchService.fetch(`${blockchain}/blocks`));

  if (isLoading) return <Loading/>;

  if (error) return <Error/>;

  return (
    
    /* Blocks table */
    <table className="table m-2 p-2">
      <thead>
        <tr>
          <th scope="col">Block Id</th>
          <th scope="col">Miner</th>
          <th scope="col">Difficulty</th>
          <th scope="col">Timestamp</th>
        </tr>
      </thead>
      <tbody>
        {data.map((block: Block) => (
          <tr key={block.id}>
            <th scope="row"><Link to={`/blocks/${block.id}`}>{block.id}</Link></th>
            <td><Link to={`/address/${block.miner}`}>{block.miner}</Link></td>
            <td>{block.difficulty}</td>
            <td>{block.timestamp}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Blocks;

