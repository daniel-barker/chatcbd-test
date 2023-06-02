import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

async function loadShoes() {
  const shoeLink = await fetch ('http://localhost:8080/api/shoes/');
  const hatsLink = await fetch ('http://localhost:8090/api/hats/');
  if (shoeLink.ok && hatsLink.ok) {
    const shoeData= await shoeLink.json();
    const hatsData= await hatsLink.json();
    root.render(
        <App shoes={shoeData.shoes} hats={hatsData.hats}/>
    );
  } else {
    console.error("SHTS FKD UP");
  }
}
loadShoes();
