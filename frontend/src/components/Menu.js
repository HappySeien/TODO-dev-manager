import React, { useState } from 'react';
import {
    MDBContainer,
    MDBNavbar,
    MDBNavbarBrand,
    MDBNavbarToggler,
    MDBIcon,
    MDBNavbarNav,
    MDBNavbarItem,
    MDBNavbarLink,
    MDBDropdown,
    MDBDropdownToggle,
    MDBDropdownMenu,
    MDBDropdownItem,
    MDBDropdownLink,
    MDBCollapse,
} from 'mdb-react-ui-kit';

function MainMenu(auth) {
    const [showBasic, setShowBasic] = useState(false);
    return (
        <MDBNavbar expand='lg' light bgColor='light'>
            <MDBContainer fluid>
                <MDBNavbarBrand href='/'>TODO manager</MDBNavbarBrand>

                <MDBNavbarToggler
                    aria-controls='navbarSupportedContent'
                    aria-expanded='false'
                    aria-label='Toggle navigation'
                    onClick={() => setShowBasic(!showBasic)}
                >
                    <MDBIcon icon='bars' fas />
                </MDBNavbarToggler>

                <MDBCollapse navbar show={showBasic}>
                    <MDBNavbarNav className='mr-auto mb-2 mb-lg-0'>
                        <MDBNavbarItem>
                            <MDBNavbarLink active aria-current='page' href='/'>
                                Home
                            </MDBNavbarLink>
                        </MDBNavbarItem>
                        
                        <MDBNavbarItem>
                            {auth.isAuth() ?
                            <MDBNavbarLink href='#' onClick={() => auth.logOut()}>Logout</MDBNavbarLink> :
                                <MDBNavbarLink href='/login'>Login</MDBNavbarLink>}
                        </MDBNavbarItem>

                        <MDBNavbarItem>
                            {auth.isAuth() ?
                                <MDBNavbarLink href='/projects/create'>Create Project</MDBNavbarLink> :
                                <> </>}
                        </MDBNavbarItem>

                        <MDBNavbarItem>
                            <MDBDropdown>
                                <MDBDropdownToggle tag='a' className='nav-link'>
                                    Menu
                                </MDBDropdownToggle>
                                <MDBDropdownMenu>
                                    <MDBDropdownItem>
                                        <MDBDropdownLink href='/users'>Users</MDBDropdownLink>
                                    </MDBDropdownItem>
                                    <MDBDropdownItem>

                                        <MDBDropdownLink href='/projects'>Projects</MDBDropdownLink>
                                    </MDBDropdownItem>
                                    <MDBDropdownItem>
                                        <MDBDropdownLink href='/notes'>Notes</MDBDropdownLink>
                                    </MDBDropdownItem>
                                </MDBDropdownMenu>
                            </MDBDropdown>
                        </MDBNavbarItem>

                        <MDBNavbarItem>
                            {auth.isAuth() ?
                            <MDBNavbarLink disabled href='#' tabIndex={-1} aria-disabled='true'>
                                 {auth.currentUser.username}
                                </MDBNavbarLink> : <MDBNavbarLink disabled href='#' tabIndex={-1} aria-disabled='true'>
                                    Anonim
                                </MDBNavbarLink>}
                        </MDBNavbarItem>
                    </MDBNavbarNav>
                </MDBCollapse>
            </MDBContainer>
        </MDBNavbar>
    );
}

export default MainMenu;
