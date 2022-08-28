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
      'users': [],
      'projects': [],
      'notes': [],
    }
  }

  isAuth () {
    return this.state.token !== ''
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
        console.log(token)
        this.setState(
          {
            'token': token
          }, this.loadData
        )
      }
      ).catch(error => console.log(error))
  }

  loadData () {
    let headers =  this.getHeaders()
    // users
    axios.get(UserApi, {headers})
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
    axios.get(ProjectApi, {headers})
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
    axios.get(NotesApi, {headers})
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
    this.loadData()
  }

  render () {
    return(
      <div className='d-flex flex-column min-vh-100'>
        <BrowserRouter>
          <nav>
            <MainMenu />
          </nav>
          <Routes>
            <Route exect path='/login' element={<LoginForm authToken={(username, password) => this.authToken(username, password)} />} />
            <Route exect path='/users' element={<UserList users={this.state.users} />} />
            <Route path='/projects'>
              <Route index element={<ProjectList projects={this.state.projects} />} />
              <Route path=':projectId' element={<ProjectInfoList 
                notes={this.state.notes} 
                developers={this.state.users} 
                projects={this.state.projects} />} />
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
