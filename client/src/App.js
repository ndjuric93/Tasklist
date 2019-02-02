import React, { Component } from 'react';
import Login from './components/Login'
import Toolbar from './components/Toolbar';
import Dashboard from './components/Dashboard';

class App extends Component {

    constructor(props) {
        super(props)
        this.state = {
            'authenticated': false,
            'current': <Login />,
        }
    }

    updateCurrent() {
        if(this.state.authenticated === false) {
            this.setState({
                'current': (
                    <React.Fragment>
                        <Toolbar />
                        <Dashboard />
                    </React.Fragment>
                ),
                'authenticated': true
            })
        } else {
            this.setState({
                'current': (<Login />),
                'authenticated': false
            })
        }
    }    

  render() {
    return (
        <React.Fragment>
            {React.cloneElement(this.state.current, {update:this.updateCurrent.bind(this)})}
        </React.Fragment>
    );
  }
}

export default App;
