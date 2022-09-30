import React, { Component, useEffect, useState } from 'react'
import EmployeeList from '../components/EmployeeList'

const EmployeeListPage = () => {
    let [employees, setEmpl] = useState([])

    useEffect(() => {
        getEmployee()
    }, [])

    let getEmployee = async () => {
        let response = await fetch('api/employees/')
        let data = await response.json()
        setEmpl(data)
    }

    return (
        <div className='notes'>
            <div className='notes-header'>
                <h2 className='notes-title'>Employes</h2>
                <p className='notes-count'>{employees.length}</p>

            </div>

        <div className='notes-list'>
            {employees.map((employee,index) => (
                <EmployeeList  key={index} employees={employee} />
            ))}
        </div>
        </div>
    )
}


export default EmployeeListPage