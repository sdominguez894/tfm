import React, { useContext } from "react";
import { useQuery } from "react-query";
import { AppContext } from "../../contexts/appContext";
import { FetchService } from "../../services/fetchService";
import Loading from "../Loading";
import Error from "../Error";
import { Transaction } from "../../Models/Transactions";
import { Link } from "react-router-dom";

const Transactions = () => {

  const { blockchain, setBlockchain } = useContext(AppContext);
  const { isLoading, error, data } = useQuery(["transactions", blockchain],
                                              () => FetchService.fetch(`${blockchain}/transactions`));

  if (isLoading) return <Loading/>;

  if (error) return <Error/>;

  return (
    <table className="table m-2 p-2">
      <thead>
          <tr>
            <th scope="col">Transaction id</th>
            <th scope="col">From</th>
            <th scope="col">To</th>
            <th scope="col">Value</th>
            <th scope="col">Block</th>
          </tr>
      </thead>
      <tbody>
        {data.map((tx: Transaction) => (
          <tr key={tx.id}>
            <th scope="row">
              {/** Show only first 5 and last 5 characters**/}
              <Link to={`/transactions/${tx.id}`}>
                {`${tx.id.substring(0, 5)}...${tx.id.substring(tx.id.length - 5)}`}
              </Link>
              </th>
            <td><Link to={`/address/${tx.from}`}>{tx.from}</Link></td>
            <td><Link to={`/address/${tx.to}`}>{tx.to}</Link></td>
            <td>{tx.value}</td>
            <td>{tx.block}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Transactions;
