import React from 'react';
import { useParams } from 'react-router-dom';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';

import { UserItem } from './User';
import { NoteItem } from './Notes';

const ProjectInfoList = ({ notes, developers, projects }) => {
    let params = useParams()
    let project = projects.filter((project) => project.id === parseInt(params.projectId))[0]
    let filteredNotes = notes.filter((note) => note.project === parseInt(params.projectId))
    let filteredUsers = developers.filter((developer) => project.developers.includes(developer.id))
    return (
    <>
        <h1 className='text-center'>{project.name}</h1>
            <p className='text-center'>{project.discroption}</p>
        <h3 className='text-center'>Developers</h3>
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
                    {filteredUsers.map((user) => <UserItem key={user.id.toString()} user={user} />)}
            </MDBTableBody>
        </MDBTable>
    
        <h3 className='text-center'>Notes</h3>
        <MDBTable className='container-md'>
            <MDBTableHead>
                <tr>
                    <th>id</th>
                    <th>title</th>
                    <th>Discroption</th>
                    <th>Author</th>
                    <th>project</th>
                </tr>
            </MDBTableHead>
            <MDBTableBody>
                {filteredNotes.map((note) => <NoteItem key={note.id.toString()} note={note} />)}
            </MDBTableBody>
        </MDBTable>
    </>
    )
}
export default ProjectInfoList;
