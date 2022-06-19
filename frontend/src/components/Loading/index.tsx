import React from "react";
import "./styles.css";

const Loading = () => {

    return (
        <>
            <div className="loading">
                <h3 className="loading__title">Loading... </h3>
                <img className="loading__img"
                     src="/loading-icon.gif" 
                     alt="Loading"/>
            </div>
        </>

    );
};

export default Loading;