/* eslint-disable react/jsx-no-comment-textnodes */
import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import './index.css';
import { AppContext, explorerContext } from "./contexts/appContext"
import App from './components/App';
import Nav from './components/Nav';
import MainPage from './routes/MainPage';
import BlocksPage from "./routes/BlocksPage";
import BlockDetailsPage from "./routes/BlockDetailsPage";
import TransactionsPage from './routes/TransactionsPage';
import TransactionDetailsPage from './routes/TransactionDetailsPage';
import { QueryClient, QueryClientProvider, useQuery } from 'react-query'
 
const queryClient = new QueryClient()

ReactDOM.render(
  <React.StrictMode>
      <QueryClientProvider client={queryClient}>
        <Router>
          <App/>
        </Router>
      </QueryClientProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
