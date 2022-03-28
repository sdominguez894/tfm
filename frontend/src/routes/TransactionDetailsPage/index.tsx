import React from 'react';
import { useParams } from 'react-router-dom';
import TransactionDetails from '../../components/TransactionDetails';

const TransactionDetailsPage = () => {

  let params = useParams();

  return (
    <div className="container mt-5">
      <TransactionDetails id={params.transactionId!} />
    </div>
  );
}

export default TransactionDetailsPage;
