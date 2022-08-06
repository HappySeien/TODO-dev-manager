import React from 'react';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';


const UserApi = 'http://127.0.0.1:8000/userapp/api/users/'

const UserItem = ({user}) => {
    return(
        <tr>
            <td>
                {user.username}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.date_of_birth}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return(
        <MDBTable className='container-md'>
            <MDBTableHead>
                <tr>
                    <th>Username</th>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Date of birth</th>
                    <th>Email</th>
                </tr>
            </MDBTableHead>
            <MDBTableBody>
                {users.map((user) => <UserItem user={user} />)}
            </MDBTableBody>  
        </MDBTable>
    )
}

export default UserList;
export {UserApi};
