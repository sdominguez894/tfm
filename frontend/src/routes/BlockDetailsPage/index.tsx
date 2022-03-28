import React from 'react';
import { useParams } from 'react-router-dom';
import BlockDetails from '../../components/BlockDetails';

const BlockDetailsPage = () => {

    let params = useParams();

    return (
      <div className="container mt-5">
        <BlockDetails id={params.blockId!} />
      </div>
    );
  }
  
  export default BlockDetailsPage;
  