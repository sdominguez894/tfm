import React from 'react';
import { useParams } from 'react-router-dom';
import Address from '../../components/Address';


const AddressPage = () => {

    let params = useParams();
  
    return (
      <div className="container mt-5">
        <Address id={params.id!} />
      </div>
    );
  }
  
  export default AddressPage;
  