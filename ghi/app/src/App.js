import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
// import HatList from './HatList';
import ShoesList from './ShoesList';


function App(shoeData) {
  if (shoeData === undefined) {
    return null;
  }
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        {/* <HatList hats={hats} /> */}
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path='shoes' element={<ShoesList shoes={shoeData}/>} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
