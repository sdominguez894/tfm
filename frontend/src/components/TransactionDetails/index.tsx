import React, { useContext } from 'react';
import { useQuery } from 'react-query';
import { Link } from "react-router-dom";
import { AppContext } from '../../contexts/appContext';
import { FetchService } from '../../services/fetchService';
import Loading from '../Loading';
import Error from '../Error';

const TransactionDetails = (props: { id : string}) => {

  const rawParam = 'raw=True';
  const { blockchain, setBlockchain } = useContext(AppContext);
  const { isLoading, error, data } = useQuery("transactionDetail", () => {
                                                const URL = `${blockchain}/transactions/${props.id}?${rawParam}`;
                                                return FetchService.fetch(URL);
                                              });

  if (isLoading) return <Loading/>;

  if (error) return <Error/>;

  return (
    <>
      <div className="card">
        <div className="card-header">
          Transaction details
        </div>
        <div className="card-body">
          <p className="card-text">
            <strong>From: </strong><Link to={`/address/${data.from}`}>{data.from}</Link>
          </p>
          <p className="card-text">
            <strong>To: </strong><Link to={`/address/${data.to}`}>{data.to}</Link>
          </p>
          <p className="card-text">
            <strong>Value: </strong>{data.value}
          </p>
          <p className="card-text">
            <strong>Block: </strong><Link to={`/blocks/${data.block}`}>{data.block}</Link>
          </p>

          {/** Raw data **/}
          <div className="accordion" id="accordionExample">
            <div className="accordion-item">
              <h2 className="accordion-header" id="headingOne">
                <button className="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                  Raw data
                </button>
              </h2>
              <div id="collapseOne" className="accordion-collapse collapse" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                <div className="accordion-body">
                  <pre>
                    {/** Show pretty printed if valid json otherwhise show string **/}
                    { 
                      JSON.parse(data.rawData) 
                      ?
                      JSON.stringify(JSON.parse(data.rawData), null, 2)
                      :
                      data.rawData
                    }
                  </pre>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default TransactionDetails;
