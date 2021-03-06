import React from 'react';
import { Link } from "react-router-dom";
import NavSearch from '../NavSearch';
import NetworksList from "../NetworksList";

const Nav = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container-fluid">
        
        <Link className="navbar-brand" aria-current="page" to="/">
          <img src="/explorer-icon.png" 
               className='pr2'
               width="100" height="auto" 
               alt="Explorer icon" />  
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link
                className="nav-link active"
                aria-current="page"
                to="/blocks"
              >
                Blocks
              </Link>
            </li>
            <li className="nav-item">
              <Link
                className="nav-link active"
                aria-current="page"
                to="/transactions"
              >
                Transactions
              </Link>
            </li>
          </ul>
          <NetworksList />
          <NavSearch />
        </div>
      </div>
    </nav>
  );
}

export default Nav;
