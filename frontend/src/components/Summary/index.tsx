import React from 'react';

const Summary = () => {

    return (
      <>
        <div className="Summary">
          {/* SUMMARY DATA */}
          <table className="table m-2 p-2">
            <thead>
                <tr>
                <th scope="col">Column 1</th>
                <th scope="col">Column 2</th>
                <th scope="col">Column 3</th>
                <th scope="col">Column 4</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                <th scope="row">Value 1</th>
                <td>Value 2</td>
                <td>Value 3</td>
                <td>Value 4</td>
                </tr>
                <tr>
                <th scope="row">Value 1</th>
                <td>Value 2</td>
                <td>Value 3</td>
                <td>Value 4</td>
                </tr>
            </tbody>
          </table>
        </div>
      </>
    );
  }
  
export default Summary;