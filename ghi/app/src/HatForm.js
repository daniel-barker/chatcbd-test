import React, { useEffect, useState } from 'react';

function HatForm () {
  const [fabric, setFabric] = useState('');
  const [styleName, setStyleName] = useState('');
  const [color, setColor] = useState('');
  const [hatPicture, setPictureUrl] = useState('')
  const [location, setLocation] = useState('')
    const [locations, setLocations] = useState([])

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
  const handlePictureChange = (event) => {
    const value = event.target.value
    setPictureUrl(value)
  }
  const handleLocationChange = (event) => {
    const value = event.target.value
    setLocation(value)
  }
  const fetchData = async () => {
    const bin = 'http://localhost:8090/api/locations/'
    const response = await fetch(location)
    if (response.ok) {
        const data = await response.json()
        setLocations(data.locations)
    }
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
  }
  const response = await fetch(hatUrl, fetchConfig);
  if (response.ok) {
    const newLocation = await response.json();
    console.log(newLocation);

    setFabric('');
    setStyleName('');
    setColor('');
  }
}

  useEffect(() => {
      fetchData();
  }, []);

    return (
        <div className="row">
        <div className="offset-3 col-6">
          <div className="shadow p-4 mt-4">
            <h1>Add a new Hat to your Wardrobe!</h1>
            <form onSubmit={handleSubmit} id="create-location-form">
              <div className="form-floating mb-3">
                <input onChange={handleFabricChange} value={fabric} placeholder={"Fabric"} required type="text" name="fabric" id="fabric" className="form-control"/>
                <label htmlFor="name">Fabric</label>
              </div>
              <div className="form-floating mb-3">
                <input onChange={handleStyleNameChange} value={styleName} placeholder="Style name" required type="number" name="style_name" id="style_name" className="form-control"/>
                <label htmlFor="room_count">Style name</label>
              </div>
              <div className="form-floating mb-3">
                <input onChange={handleColorChange} value={color} placeholder="Color" required type="text" name="color" id="color" className="form-control"/>
                <label htmlFor="color">Color</label>
              </div>
              <div className="mb-3">
                  <select onChange={handleLocationChange} value={location} required id="locations" name="locations" className="form-select">
                      <option value="">Choose a location</option>
                      {locations.map(location => {
                          return (
                            <option key={location.id} value={location.href}>
                                {location.closet_name}
                            </option>
                        )
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
