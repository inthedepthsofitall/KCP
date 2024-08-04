import React from 'react';
import URLShortener from './UrlForm';
import './App.css'; 

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>SLIMMIE DOWN THAT URL</h1>
        <div className="URLShortener-container">
          <URLShortener />
        </div>
      </header>
    </div>
  );
}

export default App;
