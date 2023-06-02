import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import HatForm from './HatForm';
import Nav from './Nav';
import HatList from './HatList';
import ShoesList from './ShoesList';


function App({shoes, hats}) {
  if (shoes === undefined || hats === undefined) {
    return null;
  }
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path='shoes' element={<ShoesList shoes={shoes}/>} />
          <Route path='hats' element={<HatList hats={hats}/>} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
