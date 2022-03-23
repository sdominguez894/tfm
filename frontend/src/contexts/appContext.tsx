import * as React from "react";

export const defaultBlockchain = "ETH"

interface AppContextInterface {
  blockchain: string;
  setBlockchain: Function
}

export const explorerContext: AppContextInterface = {
    blockchain: defaultBlockchain,
    setBlockchain: () => {}
};

export const AppContext = React.createContext<AppContextInterface>(explorerContext);