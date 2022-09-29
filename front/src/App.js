import logo from './logo.svg';
import './App.css';
import { useState, useEffect, Component } from 'react';
import EmployeeList from './components/EmployeeList';


function App() {

  const [employees, setEmpl] = useState([])
  
  
  useEffect(() =>  {
    fetch('http://127.0.0.1:8000/api/employees/', {
      'method':'GET',
      headers: {
        'Content-Type':'application/json',
        'Authorization': 'Token 7a2880cd24c321eee90c9e4d66e6a1777e2eac86'
      }
    })
    .then(resp => resp.json())
    .then(resp => setEmpl(resp))
    .catch(error => console.log(error))
  }, [])

    return (
     <div className='App'>
      <div className='col'>
      <div className='row'>
    <h2>HI</h2>
    <br/>
    </div>
      <EmployeeList employees = {employees}/>
      </div>

     </div>

    )
  }

export default App;
