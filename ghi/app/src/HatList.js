import React from 'react'

export default function HatList(props) {
    console.log("PROPS:", props)
    return (
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Fabric</th>
                    <th>Style name</th>
                </tr>
            </thead>
            <tbody>
                {props.hats?.map(hat => {
                    return (
                        <tr key={hat.id}>
                            <td>{hat.fabric}</td>
                            <td>{hat.style_name}</td>
                        </tr>
                    );
                })}
            </tbody>
        </table>);

}

// function HatList(props) {
//   const deleteHat = async (href) => {
//     const url = `http://localhost:8090/${href}`;
//     const fetchConfig = {
//         method: "delete",
//         headers: {
//             'Content-Type': 'application/json',
//         },
//     };

//     const response = await fetch(url, fetchConfig);
//     if (response.ok) {
//         window.location.reload(false);
//     }
// }
//     return (
//     <table className="table table-striped">
//         <thead>
//           <tr>
//             <th>Style</th>
//             <th>Fabric</th>
//             <th>Color</th>
//             <th>Picture</th>
//             <th>Location</th>
//           </tr>
//         </thead>
//         <tbody>
//           {props.hats.map(hat => {
//             return (
//               <tr key={hat.href}>
//                 <td>{ hat.style }</td>
//                 <td>{ hat.fabric }</td>
//                 <td>{ hat.color }</td>
//                 <td>
//                     <img src={hat.picture_url} alt="" width="75px" height="75px"/>
//                 </td>
//                 <td>{hat.location}</td>
//                 {<td>
//                   <button className="btn btn-outline-primary" onClick={() => deleteHat(hat.href)}>Delete</button>
//                 </td>}
//               </tr>
//             );
//           })}
//         </tbody>
//       </table>
//     );
//   }

//   export default HatList.js;
