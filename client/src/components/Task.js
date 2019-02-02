import React from 'react';
import PropTypes from 'prop-types';
import {
	Grid,
	Button,
	Card,
	CardActions,
	withStyles,
	Typography
} from '@material-ui/core/';
import TaskDialog from './TaskDialog'
import { editTask, deleteTask, markTaskDone } from '../providers/DataProviders'

const styles = {
	card: {
		maxWidth: 345,
		maxHeight: 300,
		backgroundColor: 'white'
	},
	title: {
		fontFamily: 'note-tracker-icon-font',
	}
};

class Task extends React.Component {

	constructor(props) {
		super(props)
		console.log(this.props.data)
        this.state = {
            'formOpen': false,
            'title': this.props.data.title,
			'description': this.props.data.description,
			'doneBy': this.props.data.done_by
		}
		console.log(this.state)
		this.handleCloseDialog = this.handleCloseDialog.bind(this)
	}

    handleForm() {
        this.setState({
            'formOpen': !this.state.formOpen
        })
    }

    handleCloseDialog(data) {
		this.setState({ 'formOpen': false })
		editTask(this.props.data.id, data).then(() =>  this.props.update())
	}
	
	markDone() {
		markTaskDone(this.props.data.id).then(() => this.props.update())
	}

	delete() {
		deleteTask(this.props.data.id).then(() => this.props.update())
	}

	render() {
		const { classes } = this.props;
		console.log(this.props.data)
		return (
			<div>
				<Card className={classes.card} >
					<div>
						<Typography gutterBottom variant="headline" component="h2" className={classes.title}>
							{this.props.data.title}
							{"(created by " +this.props.data.user + ")"}
						</Typography>
						<Typography  className={classes.title}>
							{this.props.data.description}
						</Typography>
					</div>
					<CardActions>
						<Grid container justify='center' spacing={16}>
							<Grid item>
								<Button 
									variant='contained' 
									color='primary' 
									size='small'
									onClick={() => this.handleForm()}
								>
									Edit
                        		</Button>
								<TaskDialog 
									open={this.state.formOpen}
									closeDialog={this.handleCloseDialog}
									title={this.state.title}
									description={this.state.description}
								/>
							</Grid>
							<Grid item>
								<Button 
									variant='contained'
									color='primary' 
									size='small' 
									onClick={() => this.delete()}
								>
									Delete
                        		</Button>
							</Grid>
							<Grid item>
								<Button 
									variant='contained'
									color={this.props.data.done_by !== undefined ? "default" : "secondary"}
									size='small'
									onClick={() => this.markDone()}
									disabled={this.props.data.done_by !== undefined}
								>
									{this.props.data.done_by === undefined ? "Mark done" : this.props.data.done_by + " ✓"}
								</Button>
							</Grid>
						</Grid>
					</CardActions>
				</Card>
			</div>
		);
	}
}

Task.propTypes = {
	classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Task);
