import React from 'react';
import './App.css';
import axios from 'axios';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom'

import LoginForm from './components/auth';
import UserList from './components/User';
import ProjectList from './components/Projects';
import ProjectInfoList from './components/PorjectInfo';
import NotesList from './components/Notes';

import { tokenApi } from './components/auth';
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
      'token': '',
      'currentUser': '',
      'users': [],
      'projects': [],
      'notes': [],
      'redirect': false,
    }
  }

  isAuth () {
    return !!this.state.token != ''
  }

  logOut () {
    localStorage.setItem('token', '')
    localStorage.setItem('currentUser', '')
    this.setState(
      {
        'token': '',
        'currentUser': ''
      }, this.loadData
    )
  }

  getHeaders () {
    if(this.isAuth()) {
      return {'Authorization': `Token ${this.state.token}`}
    }
    return {}
  }

  authToken(username, password) {
    axios.post(tokenApi, { 'username': username, 'password': password})
      .then(response => {
        const token = response.data.token
        localStorage.setItem('token', token)
        localStorage.setItem('currentUser', username)
        this.setState(
          {
            'token': token,
            'currentUser': username,
            'redirect': '/'
          }, this.loadData
        )
      }
      ).catch(error => console.log(error))
  }

  deleteProject(projectId) {
    let headers = this.getHeaders()

    axios
      .delete(`${ProjectApi}${projectId}`, { headers })
      .then(response => {
        this.setState({
          'projects': this.state.projects.filter((project) => project.id != projectId)
        })
      })
      .catch(error => {
        console.log(error)
      })
  }

  deleteNote(noteId) {
    let headers = this.getHeaders()

    axios
      .delete(`${NotesApi}${noteId}`, { headers })
      .then(response => {
        this.setState({
          'notes': this.state.projects.filter((note) => note.id != noteId)
        })
      })
      .catch(error => {
        console.log(error)
      })
  }

  loadData () {
    this.setState({
      'redirect': false
    })

    let headers =  this.getHeaders()
    // users
    axios.get(UserApi, { headers })
      .then(response => {
        const users = response.data.results
        this.setState(
          {
            'users': users
          }
        )
      }
      ).catch(error => console.log(error))

    // projects
    axios.get(ProjectApi, { headers })
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
    axios.get(NotesApi, { headers })
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

  componentDidMount() {
    let token = localStorage.getItem('token')
    let username = localStorage.getItem('currentUser')
    this.setState(
      {
        'token': token,
        'currentUser': username
      }, this.loadData
    )
  }

  render () {
    return(
      <div className='d-flex flex-column min-vh-100'>
        <BrowserRouter>
          {this.state.redirect ? <Navigate to={this.state.redirect} replace={true} /> : <div />}
          <nav>
            <MainMenu isAuth={() => this.isAuth()} logOut={() => this.logOut()} currentUser={this.state.currentUser} />
          </nav>
          <Routes>
            <Route exect path='/login' element={<LoginForm authToken={(username, password) => this.authToken(username, password)} />} />
            <Route exect path='/users' element={<UserList users={this.state.users} />} />
            <Route path='/projects'>
              <Route index element={<ProjectList projects={this.state.projects} deleteProject={(projectId) => this.deleteProject(projectId)} />} />
              <Route path=':projectId' element={<ProjectInfoList 
                notes={this.state.notes} 
                developers={this.state.users} 
                projects={this.state.projects} />} />
            </Route>
            <Route exect path='/notes' element={<NotesList notes={this.state.notes} deleteNote={(noteId) => this.deleteNote(noteId)} />} />
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
