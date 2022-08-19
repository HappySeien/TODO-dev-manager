import React from 'react';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';


const NotesApi = 'http://localhost:8000/api/notes/'

const NoteItem = ({ note }) => {
    return (
        <tr>
            <td>
                {note.id}
            </td>
            <td>
                {note.title}
            </td>
            <td>
                {note.discroption}
            </td>
            <td>
                {note.author}
            </td>
            <td>
                {note.project}
            </td>
        </tr>
    )
}

const NotesList = ({ notes }) => {
    return (
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
                {notes.map((note) => <NoteItem key={note.id.toString()} note={note} />)}
            </MDBTableBody>
        </MDBTable>
    )
}

export default NotesList;
export { NotesApi, NoteItem };
