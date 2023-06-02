import React, { useState, useEffect } from "react"

function ShoeForm() {
    const [shoeMake, setManufacturer] = useState('')
    const [shoeModel, setModelName] = useState('')
    const [shoeColor, setColor] = useState('')
    const [shoePicture, setPictureUrl] = useState('')
    const [bin, setBin] = useState('')
    const [bins, setBins] = useState([])

    const handleMakeChange = (event) => {
        const value = event.target.value
        setManufacturer(value)
    }
    const handleModelChange = (event) => {
        const value = event.target.value
        setModelName(value)
    }
    const handleColorChange = (event) => {
        const value = event.target.value
        setColor(value)
    }
    const handlePictureChange = (event) => {
        const value = event.target.value
        setPictureUrl(value)
    }
    const handleBinChange = (event) => {
        const value = event.target.value
        setBin(value)
    }
    const fetchData = async () => {
        const bin = 'http://localhost:8100/api/bins/'
        const response = await fetch(bin)
        if (response.ok) {
            const data = await response.json()
            setBins(data.bins)
        }
    }


    const handleSubmit = async (event) => {
        event.preventDefault()
        const data = {}
        data.shoe_make = shoeMake
        data.shoe_model = shoeModel
        data.shoe_color = shoeColor
        data.shoe_picture = shoePicture
        data.bin = bin

        const shoesUrl = "http://localhost:8080/api/shoes/"
        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
            },
        }

        const response = await fetch(shoesUrl, fetchConfig)
        if (response.ok) {
            const newBin = await response.json()
            console.log(newBin)

            setManufacturer('')
            setModelName('')
            setColor('')
            setPictureUrl('')
            setBin('')
        }
    }

    useEffect(() => {
        fetchData()
    }, [])

    return (
        <div className="row">
            <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                    <h1>Add Shoes to Your Wardrobe!</h1>
                    <form onSubmit={handleSubmit} id="create-bin-form">
                        <div className="form-floating mb-3">
                            <input onChange={handleMakeChange} value={shoeMake} placeholder="Make" required type="text" name="shoe_make" id="shoe_make" className="form-control" />
                            <label htmlFor="shoe_make">Shoe Maker</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input onChange={handleModelChange} value={shoeModel} placeholder="Model" required type="text" name="shoe_model" id="shoe_model" className="form-control" />
                            <label htmlFor="shoe_model">Model</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input onChange={handleColorChange} value={shoeColor} placeholder="Color" required type="text" name="shoe_color" id="shoe_color" className="form-control" />
                            <label htmlFor="shoe_color">Color</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input onChange={handlePictureChange} value={shoePicture} placeholder="Picture Url" required type="text" name="shoe_picture" id="shoe_picture" className="form-control" />
                            <label htmlFor="shoe_picture">Picture URL</label>
                        </div>
                        <div className="mb-3">
                            <select onChange={handleBinChange} value={bin} required id="bins" name="bins" className="form-select">
                                <option value="">Choose a bin</option>
                                {bins.map(bin => {
                                    return (
                                        <option key={bin.id} value={bin.href}>
                                            {bin.closet_name}
                                        </option>
                                    )
                                })}
                            </select>
                        </div>
                        <button className="btn btn-primary">Add!</button>
                    </form>
                </div>
            </div>
        </div>

    )
}

export default ShoeForm;
