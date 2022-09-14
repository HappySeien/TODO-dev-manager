import React from 'react';
import { MDBTable, MDBTableHead, MDBTableBody, MDBIcon, MDBBtn } from 'mdb-react-ui-kit';


const NotesApi = 'http://localhost:8000/api/notes/'

const NoteItem = ({ note, deleteNote }) => {
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
            <td>
                <MDBBtn onClick={() => deleteNote(note.id)} color='link'><MDBIcon fas icon="archive" /></MDBBtn>
            </td>
        </tr>
    )
}

const NotesList = ({ notes, deleteNote }) => {
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
                {notes.map((note) => <NoteItem key={note.id.toString()} note={note} deleteNote={deleteNote} />)}
            </MDBTableBody>
        </MDBTable>
    )
}

export default NotesList;
export { NotesApi, NoteItem };
