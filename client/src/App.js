import React, { Component } from 'react';
import Login from './components/Login'

class App extends Component {

    constructor(props) {
        super(props)
        this.state = {
            'current': <Login />
        }
    }

  render() {
    return (
        <React.Fragment>
            {this.state.current}
        </React.Fragment>
    );
  }
}

export default App;
