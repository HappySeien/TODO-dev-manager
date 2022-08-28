import React from "react";
import {
    MDBInput,
    MDBCol,
    MDBRow,
    MDBCheckbox,
    MDBBtn
} from 'mdb-react-ui-kit';

const tokenApi = 'http://127.0.0.1:8000/api-token-auth/'


class LoginForm extends React.Component {
    constructor (props) {
        super (props)
        this.state = {
            'username': '',
            'password': ''
        }
    }

    handleChange (event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
    }

    handleSubmit (event) {
        event.preventDefault()
        this.props.authToken(this.state.username, this.state.password)
    }

    render () {
        return (
            <div className='d-flex mx-auto my-auto'>
                <form onSubmit={(event) => this.handleSubmit(event) }>
                    <MDBInput className='mb-4' type='text' id='username' name='username' label='Username' value={this.state.username} 
                        onChange={ (event) => this.handleChange(event) } />
                    <MDBInput className='mb-4' type='password' id='password' name='password' label='Password' value={this.state.password} 
                        onChange={(event) => this.handleChange(event) } />

                    <MDBRow className='mb-4'>
                        <MDBCol className='d-flex justify-content-center'>
                            <MDBCheckbox id='form1Example3' label='Remember me' defaultChecked />
                        </MDBCol>
                        <MDBCol>
                            <a href='#!'>Forgot password?</a>
                        </MDBCol>
                    </MDBRow>

                    <MDBBtn type='submit' block>
                        Sign in
                    </MDBBtn>
                </form>
            </div>
        )
    }
}

export default LoginForm;
export {tokenApi};