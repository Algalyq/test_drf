
import React, { useEffect, useState } from 'react'
import axios from 'axios';
axios.defaults.withCredentials = true;

function EmployeeList(props) {
    const [employees, setEmpl] = useState([])
    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/employees/', {
            'method':'GET',
            headers: {
              'Content-Type':'application/json',
              'Authorization': 'Token 7a2880cd24c321eee90c9e4d66e6a1777e2eac86'
            }
          })
    }, []);
    
    const apiURL = "http://127.0.0.1:8000/api/employees/";
    const fetchData = async() => {
      const response = await axios.get(apiURL,
        {'withCredentials': true});
      console.log(response);
      setEmpl(response.data);
      console.log(employees);
      console.log(response.data);
      
    }
    return (
        <div>
         {props.employees.map (employee => {
        return (
    <div key={employee.id} >
       <h2>{employee.Surename_empl}</h2>
          
          </div>
       
    )})}
            
        </div>
    )
}

export default EmployeeList;