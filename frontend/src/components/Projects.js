import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { MDBTable, MDBTableHead, MDBTableBody, MDBIcon, MDBBtn, MDBInput } from 'mdb-react-ui-kit';


const ProjectApi = 'http://localhost:8000/api/projects/'

const ProjectItem = ({ project, deleteProject }) => {
    return (
        <tr>
            <td>
                {project.id}
            </td>
            <td>
                <Link to={`/projects/${project.id}`}>{project.name}</Link>
            </td>
            <td>
                {project.discroption}
            </td>
            <td>
                {project.author}
            </td>
            <td>
                {project.developers}
            </td>
            <td>
                <MDBBtn onClick={() => deleteProject(project.id)} color='link'><MDBIcon fas icon="archive" /></MDBBtn>
            </td>
        </tr>
    )
}

const ProjectList = ({ projects, deleteProject }) => {
    const [value, setValue] = useState('')
    const filtredProject = projects.filter(project => {
        return project.name.toLowerCase().includes(value.toLowerCase())
    })
    return (
    <>
            <h1 className='text-center'>Projects</h1>
            <div className='d-flex mx-auto container-md'>
                <form>
                    <span>Search</span>
                    <MDBInput label='Project name' id='search' name='search' type='text' onChange={(event) => setValue(event.target.value)} />
                </form>
            </div>
        <MDBTable className='container-md'>
            <MDBTableHead>
                <tr>
                    <th>id</th>
                    <th>Name</th>
                    <th>Discroption</th>
                    <th>Author</th>
                    <th>Developers</th>
                </tr>
            </MDBTableHead>
            <MDBTableBody>
                    {filtredProject.map((project) => <ProjectItem key={project.id.toString()} project={project} deleteProject={deleteProject}/>)}
            </MDBTableBody>
        </MDBTable>
    </>
    )
}

export default ProjectList;
export { ProjectApi };
