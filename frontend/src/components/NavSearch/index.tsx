import React, { SyntheticEvent, useContext, useState } from 'react';
import { Link, useNavigate } from "react-router-dom";
import { AppContext } from '../../contexts/appContext';
import { FetchService } from '../../services/fetchService';

const NavSearch = () => {
  let navigate = useNavigate()

  const { blockchain, setBlockchain } = useContext(AppContext);
  
  const [searchText, setSearchText] = useState("");
  const state = { searchText, setSearchText };

  async function searchResource() {
    //Search endpoint
    const data = await FetchService.fetch(`${blockchain}/search/${searchText}`);

    switch (data.type) {
      case "address":
        navigate(`/address/${data.data.address}`);
        break;
      case "block":
        navigate(`/blocks/${data.data.id}`);
        break;
      case "transaction":
        navigate(`/transactions/${data.data.id}`);
        break;
      default:
        //No matching type
        alert("Element not found")
    }

  }

  return (
    <div className="d-flex">
      <input
        className="form-control me-2"
        type="search"
        placeholder="Search"
        aria-label="Search"
        value={state.searchText} 
        onChange={(event) => setSearchText(event.target.value)}
      />
      <button type="submit" 
              className="btn btn-outline-success" 
              onClick={searchResource}>
        Search
      </button>
    </div>
  );
}

export default NavSearch;
