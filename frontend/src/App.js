import React from 'react';
import './App.css';
import axios from 'axios';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom'

import UserList from './components/User';
import ProjectList from './components/Projects';
import ProjectInfoList from './components/PorjectInfo';
import NotesList from './components/Notes';

import { UserApi } from './components/User';
import { ProjectApi } from './components/Projects';
import { NotesApi } from './components/Notes';

import MainMenu from './components/Menu';
import Footer from './components/Footer';
import NotFound404 from './components/404NotFound';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'projects': [],
      'notes': [],
    }
  }

  componentDidMount() {
    // users
    axios.get(UserApi)
    .then(response =>{
      const users = response.data.results
        this.setState(
          {
            'users': users
          }
        )
      }
    ).catch(error => console.log(error))

    // projects
    axios.get(ProjectApi)
      .then(response => {
        const projects = response.data.results
        this.setState(
          {
            'projects': projects
          }
        )
      }
    ).catch(error => console.log(error))

    // notes
    axios.get(NotesApi)
      .then(response => {
        const notes = response.data.results
        this.setState(
          {
            'notes': notes
          }
        )
      }
    ).catch(error => console.log(error))
  }

  render () {
    return(
      <div className='d-flex flex-column min-vh-100'>
        <BrowserRouter>
          <nav>
            <MainMenu />
          </nav>
          <Routes>
            <Route exect path='/users' element={<UserList users={this.state.users} />} />
            <Route path='/projects'>
              <Route index element={<ProjectList projects={this.state.projects} />} />
              <Route path=':projectId' element={<ProjectInfoList notes={this.state.notes} developers={this.state.users} projects={this.state.projects}/>} />
            </Route>
            <Route exect path='/notes' element={<NotesList notes={this.state.notes} />} />
            <Route path='*' element={<NotFound404 />} />
            <Route exect path='/' element={<Navigate to='/projects' />} />
          </Routes>
          <Footer />
        </BrowserRouter>
      </div>
    )
  }
}

export default App;
