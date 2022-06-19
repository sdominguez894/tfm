import './styles.css';
import React, { useContext } from 'react';
import { useQuery } from 'react-query';
import { Link } from "react-router-dom";
import { AppContext } from '../../contexts/appContext';
import { FetchService } from '../../services/fetchService';
import Loading from '../Loading';
import Error from '../Error';

const Summary = () => {

  const rawParam = 'raw=True';
  const { blockchain } = useContext(AppContext);
  const { isLoading, error, data } =  useQuery(["summary", blockchain], () => FetchService.fetch(`${blockchain}/summary`));


  if (isLoading) return <Loading/>;

  if (error) return <Error/>;

    return (
      <>
        <div className="Summary">
          {/* SUMMARY DATA */}
          <div className="Summary__item">
            <div className="Summary__item__label"><strong>Name</strong></div>
            <div className="Summary__item__data">{data.name}</div>
          </div>
          <div className="Summary__item">
            <div className="Summary__item__label"><strong>Price</strong></div>
            <div className="Summary__item__data">{data.price} $</div>
          </div>
          <div className="Summary__item">
            <div className="Summary__item__label"><strong>Market cap</strong></div>
            <div className="Summary__item__data">{data.marketCap}</div>
          </div>
          <div className="Summary__item">
            <div className="Summary__item__label"><strong>Total supply</strong></div>
            <div className="Summary__item__data">{data.totalSupply}</div>
          </div>
          {/*
            marketCap
            totalSupply 
          */}


        </div>
      </>
    );
  }
  
export default Summary;