import React, { useEffect, useState } from 'react';

function HatForm () {
  const [states, setStates] = useState([]);
  const [fabric, setFabric] = useState('');
  const [styleName, setStyleName] = useState('');
  const [color, setColor] = useState('');

  const handleFabricChange = (event) => {
    const value = event.target.value;
    setFabric(value);
  }
  const handleStyleNameChange = (event) => {
    const value = event.target.value;
    setStyleName(value);
  }
  const handleColorChange = (event) => {
    const value = event.target.value;
    setColor(value);
  }
  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = {};

    data.fabric = fabric;
    data.style_name = styleName;
    data.color = color;

    const hatUrl = 'http://localhost:8090/api/hats/';
    const fetchConfig = {
    method: "post",
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const response = await fetch(hatUrl, fetchConfig);
  if (response.ok) {
    const newHat = await response.json();
    console.log(newHat);

    setFabric('');
    setStyleName('');
    setColor('');
  }
  const fetchData = async () => {
    const url = 'http://localhost:8000/api/hats/';

    const response = await fetch(url);

    if (response.ok) {
      const data = await response.json();
      }

    }
  }

  useEffect(() => {
    // fetchData();
  }, []);

    return (
        <div className="row">
        <div className="offset-3 col-6">
          <div className="shadow p-4 mt-4">
            <h1>Add a new hat</h1>
            <form onSubmit={handleSubmit} id="create-hat-form">
              <div className="form-floating mb-3">
                <input onChange={handleFabricChange} placeholder="Fabric" required type="text" name="fabric" id="fabric" className="form-control" value={fabric}/>
                <label htmlFor="name">Fabric</label>
              </div>
              <div className="form-floating mb-3">
                <input onChange={handleStyleNameChange} placeholder="Style name" required type="number" name="style_name" id="style_name" className="form-control" value={styleName}/>
                <label htmlFor="room_count">Style name</label>
              </div>
              <div className="form-floating mb-3">
                <input onChange={handleColorChange} placeholder="Color" required type="text" name="color" id="color" className="form-control" value={color}/>
                <label htmlFor="color">Color</label>
              </div>
              <div className="mb-3">
                <select required name="hat" id="hat" className="form-select">
                  <option selected value="">Choose a hat</option>
                  {/* need some work here */}
                  {states.map(hat => {
                    return (
                      <option key={hat.href} value={hat.href}>
                        {hat.closet_name}
                      </option>
                    );
                  })}
                </select>
              </div>
              <button className="btn btn-primary">Create</button>
            </form>
          </div>
        </div>
      </div>
    );
}

export default HatForm;
