import React from 'react'
export default function ShoesList(props) {
    console.log("PROPS:", props)
    return (
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Shoe Make</th>
                    <th>Shoe Model</th>
                </tr>
            </thead>
            <tbody>
                {props.shoes.shoes?.map(shoe => {
                    return (
                        <tr key={shoe.id}>
                            <td>{shoe.shoe_make}</td>
                            <td>{shoe.shoe_model}</td>
                        </tr>
                    );
                })}
            </tbody>
        </table>);

}
