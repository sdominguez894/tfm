import React, { useState } from "react";
import { Route, Router, Routes } from "react-router-dom";
import { AppContext, defaultBlockchain } from "../../contexts/appContext";
import BlockDetailsPage from "../../routes/BlockDetailsPage";
import BlocksPage from "../../routes/BlocksPage";
import MainPage from "../../routes/MainPage";
import TransactionDetailsPage from "../../routes/TransactionDetailsPage";
import TransactionsPage from "../../routes/TransactionsPage";
import Nav from "../Nav";

const App = () => {

    //The selected blockchain is a global state
    const [blockchain, setBlockchain] = useState(defaultBlockchain); //TODO - Load dynamically
    const state = { blockchain, setBlockchain };

    return (
        <>
            <AppContext.Provider value={state}>
                {/* Nav element is always visible */}
                <Nav/>
            
                {/* Show different content based on route */}
                <Routes>
                    <Route path="/" element={<MainPage />} />
                    <Route path="blocks" element={<BlocksPage />} />
                    <Route path="transactions" element={<TransactionsPage />} />
                    <Route path="blocks/:blockId" element={<BlockDetailsPage />} />
                    <Route path="transactions/:transactionId" element={<TransactionDetailsPage />} />
                </Routes>
            </AppContext.Provider>
        </>

    );
};

export default App;