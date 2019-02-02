import React from 'react';
import PropTypes from 'prop-types';
import { Button, GridList, GridListTile } from '@material-ui/core/';
import withStyles from '@material-ui/core/styles/withStyles';
import Task from './Task'
import TaskDialog from './TaskDialog'

import { getTasks, createTask } from '../providers/DataProviders'

const styles = theme => ({
    root: {
        display: 'flex',
        flexWrap: 'wrap',
        justifyContent: 'space-around',
        overflow: 'hidden',
        backgroundColor: theme.palette.background.paper
    },
    gridList: {
        width: '100%',
        height: '100%',
        paddingTop: '100px'
    },
    button: {
        position: "fixed",
        width: "100%",
        bottom: "0",
    }
});


class Dashboard extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'formOpen': false,
            'title': '',
            'description': '',
            'tasks': []
        }
        this.handleCloseDialog = this.handleCloseDialog.bind(this)
    }

    handleForm() {
        this.setState({
            'formOpen': !this.state.formOpen,
        })
    }

    handleCloseDialog(data) {
        this.setState({ 'formOpen': false })
        createTask(data).then(() => this.fetchTasks())
    }

    fetchTasks() {
        getTasks().then(response => {
            if(response.status === 200) {
                this.setState({'tasks': response.data})
            }
        })
    }

    componentWillMount() {
        this.fetchTasks()
    }

    render() {
        const { classes } = this.props
        return (
            <React.Fragment>
                <div className={classes.root}>
                    <GridList cellHeight={250} className={classes.gridList} cols={4} padding={2} >
                        {this.state.tasks.map(task => (
                            <GridListTile key={task.id}>
                                <Task
                                    data={task}
                                    update={this.fetchTasks.bind(this)}
                                />
                            </GridListTile>
                        ))}
                    </GridList>
                </div>
                <Button
                    variant="contained"
                    color="primary"
                    size="large"
                    className={classes.button}
                    onClick={() => this.handleForm()}
                >
                    Add new task
                </Button>
                <TaskDialog
                    open={this.state.formOpen}
                    closeDialog={this.handleCloseDialog}
                    title=''
                    description=''
                    update={this.fetchTasks.bind(this)}
                />
            </React.Fragment>
        )
    }
}

Dashboard.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Dashboard);