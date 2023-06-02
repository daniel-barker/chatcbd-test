import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

async function loadShoesAndHats() {
  const shoeLink = await fetch ('http://localhost:8080/api/shoes/');
  const hatLink = await fetch ('http://localhost:8090/api/hats/');
  if (shoeLink.ok && hatLink.ok) {
    const shoeData= await shoeLink.json();
    const hatData= await hatLink.json();
    root.render(
        <App shoes={shoeData.shoes} hats={hatData.hats}/>
    );
  } else {
    console.error("is bad");
  }
}
loadShoesAndHats();
