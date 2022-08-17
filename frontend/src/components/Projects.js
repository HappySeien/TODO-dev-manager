import React from 'react';
import { Link } from 'react-router-dom';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';


const ProjectApi = 'http://localhost:8000/api/projects/'

const ProjectItem = ({ project }) => {
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
        </tr>
    )
}

const ProjectList = ({ projects }) => {
    return (
    <>
        <h1 className='text-center'>Projects</h1>
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
                {projects.map((project) => <ProjectItem key={project.id.toString()} project={project} />)}
            </MDBTableBody>
        </MDBTable>
    </>
    )
}

export default ProjectList;
export { ProjectApi };
