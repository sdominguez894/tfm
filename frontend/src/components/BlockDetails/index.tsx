import React, { useContext } from 'react';
import { useQuery } from 'react-query';
import { Link } from "react-router-dom";
import { AppContext } from '../../contexts/appContext';
import { FetchService } from '../../services/fetchService';
import Loading from '../Loading';
import Error from '../Error';

const BlockDetails = (props: { id: string }) => {
   
  const rawParam = 'raw=True';
  const { blockchain, setBlockchain } = useContext(AppContext);
  const { isLoading, error, data } = useQuery(["blockDetails", blockchain], () => {
                                                const URL = `${blockchain}/blocks/${props.id}?${rawParam}`;
                                                return FetchService.fetch(URL);
                                              });

  if (isLoading) return <Loading/>;

  if (error) return <Error/>;

  const isParseable = (rawData: string) => {
    try {
      return JSON.parse(rawData);
    } catch(e) {
      return false;
    }
  }

  const isEmpty = (obj: any) => {
    return obj // null and undefined check
           && Object.keys(obj).length === 0
           && Object.getPrototypeOf(obj) === Object.prototype;
  }

  const escapeHtml = (unsafe: string) => {
    return unsafe.replaceAll('&', '&amp;')
                 .replaceAll('<', '&lt;')
                 .replaceAll('>', '&gt;')
                 .replaceAll('"', '&quot;')
                 .replaceAll("'", '&#039;');
  }

  return (
    <>
      <div className="card">
        <div className="card-header">
          Transaction details
        </div>
        <div className="card-body">
          <p className="card-text">
            <strong>Block number: </strong>{data.id}
          </p>
          <p className="card-text">
            <strong>Miner: </strong><Link to={`/address/${data.miner}`}>{data.miner}</Link>
          </p>
          <p className="card-text">
            <strong>Difficulty: </strong>{data.difficulty}
          </p>
          <p className="card-text">
            <strong>Timestamp: </strong>{data.timestamp}
          </p>
          
          {/** Raw data (show only if found / not empty)**/}
          { !isEmpty(data.rawData) &&
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
                      {/** Show pretty printed json if valid json otherwhise show string **/}
                      { 
                        isParseable(data.rawData) 
                        ?
                        JSON.stringify(JSON.parse(data.rawData), null, 2)
                        :
                        escapeHtml(data.rawData)
                      }
                    </pre>
                  </div>
                </div>
              </div>
            </div>
          }
          
        </div>
      </div>
    </>
  );
}

export default BlockDetails;
