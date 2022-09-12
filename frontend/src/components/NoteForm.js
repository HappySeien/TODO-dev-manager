import React from 'react'

class NoteForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'author': '',
            'project': '',
            'title': '',
            'discroption': ''
        }
    }
}

export default NoteForm;
