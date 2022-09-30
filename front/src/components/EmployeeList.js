

import { Link } from 'react-router-dom'
import React, { useEffect, useState } from 'react'

const EmployeeList = ({ employees }) => {
  return (
    <Link to={`/api/employees`}>
      <div className='notes-list-item'>
        <h3>{employees.Surename_empl}</h3>
      </div>
    </Link>
  )
}

export default EmployeeList




 // import axios from 'axios';
// axios.defaults.withCredentials = true;

// function EmployeeList(props) {
//     const [employees, setEmpl] = useState([])
//     useEffect(() => {
//         fetch('http://127.0.0.1:8000/api/employees/', {
//             'method':'GET',
//             headers: {
//               'Content-Type':'application/json',
//               'Authorization': 'Token 7a2880cd24c321eee90c9e4d66e6a1777e2eac86'
//             }
//           })
//     }, []);
    

//     const editBtn = (employee) => {
//         props.editBtn(employee)
//     }

//     const apiURL = "http://127.0.0.1:8000/api/employees/";
//     const fetchData = async() => {
//       const response = await axios.get(apiURL,
//         {'withCredentials': true});
//       console.log(response);
//       setEmpl(response.data);
//       console.log(employees);
//       console.log(response.data);
      
//     }
//     return (
//         <div>
//          {props.employees.map (employee => {
//         return (
//     <div key={employee.id} className="divEm">
//        <p > Surename: {employee.Surename_empl} </p>
//         <p> Name: {employee.Name_empl}</p>
//         <p> Post of employee: {employee.Post}</p>
//         <div className="row"> 
//             <div className="col">
//                 <button className='btn btn-primary' onClick={() => editBtn(employee) }>Update</button> 
           
//                 <button className='btn btn-danger'>Delete</button>
//             </div>    
//         </div>
//           </div>
       
//     )})}
            
//         </div>
//     )
// }

// export default EmployeeList;