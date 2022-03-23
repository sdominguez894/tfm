import './index.css';
import React, { useContext } from 'react';
import Summary from '../../components/Summary';
import Blocks from '../../components/Blocks';
import Transactions from '../../components/Transactions';
import { AppContext } from '../../contexts/appContext';

const MainPage = () => {
  
  const { blockchain } = useContext(AppContext);

  return (
    
    <div className="MainPage">

      {/* SUMMARY */}
      <div className="container mt-5">
        <h3>{blockchain} Network summary</h3>
        <div className="card">
          <div className="card-body">
              <Summary />
          </div>
        </div>
      </div>

      <div className="container mt-5">
        <h3>Blocks and transactions</h3>
        {/* TAB LINKS (Blocks and transactions) */}
        <nav>
          <div className="nav nav-tabs" id="nav-tab" role="tablist">
            <button className="nav-link active" id="nav-blocks-tab" data-bs-toggle="tab" 
                    data-bs-target="#nav-blocks" type="button" role="tab" 
                    aria-controls="nav-blocks" aria-selected="true">
                Blocks    
            </button>
            <button className="nav-link" id="nav-transactions-tab" data-bs-toggle="tab" 
                    data-bs-target="#nav-transactions" type="button" role="tab" 
                    aria-controls="nav-transactions" aria-selected="false">
                Transactions    
            </button>
          </div>
        </nav>

        {/* TAB CONTENTS (Blocks and transactions) */}
        <div className="tab-content" id="nav-tabContent">
          <div id="nav-blocks" className="tab-pane fade show active" 
              role="tabpanel" aria-labelledby="nav-blocks-tab">
              
            {/* Blocks table */}
            <Blocks />

          </div>
          <div id="nav-transactions" className="tab-pane fade" 
              role="tabpanel" aria-labelledby="nav-transactions-tab">

              {/* Transactions table */}
              <Transactions />

          </div>
        </div>
      </div>
    </div>

  );
}

export default MainPage;
