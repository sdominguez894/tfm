import React, { useContext } from "react";
import { useQuery } from "react-query";
import { AppContext } from "../../contexts/appContext";
import { FetchService } from "../../services/fetchService";
import Loading from "../Loading";
import Error from "../Error";


const Address = (props: { id: string } ) => {

  const { blockchain, setBlockchain } = useContext(AppContext);
  const { isLoading, error, data } = useQuery("address", 
                                              () => FetchService.fetch(`${blockchain}/address/${props.id}`));

  if (isLoading) return <Loading/>;

  if (error) return <Error/>;

  return (
    <>
      <h2>Address {data.address}</h2>
      <h3>Balance: {data.balance}</h3>
    </>
  );
}

export default Address;

