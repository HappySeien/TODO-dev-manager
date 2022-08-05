import React from 'react';
import './App.css';
import UserList from './components/User';
import { UserApi } from './components/User';
import axios from 'axios';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': []
    }
  }
  componentDidMount() {
    axios.get(UserApi)
    .then(response =>{
      const users = response.data
        this.setState(
          {
            'users': users
          }
        )
      }
    ).catch(error => console.log(error))
  }
  render () {
    return(
      <div className="container">
        <UserList users = {this.state.users}/>
      </div>
    )
  }
}

export default App;
