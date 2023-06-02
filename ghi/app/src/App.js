import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import HatForm from './HatForm';
import Nav from './Nav';
import HatList from './HatList';


function App(props) {
  if (props.hats === undefined) {
    return null;
  }
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route index element={<MainPage />} />
          <Route path="hats">
            <Route path="new" element={<HatForm />} />
          </Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
