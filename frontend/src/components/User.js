import React from "react";

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
                {user.age}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return(
        <table>
            <th>
                Username
            </th>
            <th>
                First Name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Age
            </th>
            <th>
                Email
            </th>
            {users.map((user) => <UserItem user = {user}/>)}
        </table>
    )
}

export default UserList;
export {UserApi};
