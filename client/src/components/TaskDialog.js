import React from 'react';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogTitle from '@material-ui/core/DialogTitle';

class TaskDialog extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'title': this.props.title,
            'description': this.props.description,
            'initialTitle': this.props.title,
            'initialDescription': this.props.description
        }
    }

    handleChange(name, event) {
        this.setState({
            [name]: event.target.value,
        });
    }

    handleRequestClose = () => {
        this.setState({ open: false });
    };

    render() {
        return (
            <div>
                <Dialog
                    open={this.props.open}
                    onClose={this.handleClose}
                    aria-labelledby="form-dialog-title"
                >
                    <DialogTitle id="form-dialog-title">Subscribe</DialogTitle>
                    <DialogContent>
                        <TextField
                            autoFocus
                            margin="dense"
                            id="title"
                            label="Title"
                            fullWidth
                            value={this.state.title}
                            onChange={(event) => this.handleChange('title', event)}
                        />
                        <TextField
                            autoFocus
                            margin="dense"
                            id="description"
                            label="Description"
                            fullWidth
                            multiline
                            rowsMax="4"
                            value={this.state.description}
                            onChange={(event) => this.handleChange('description', event)}
                        />
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={() => {
                                    this.setState({
                                        'title': this.state.initialTitle,
                                        'description': this.state.initialDescription
                                    })
                                    this.props.closeDialog({
                                        'title': this.state.title,
                                        'description': this.state.description
                                    })
                                }
                            }
                            color="primary"
                        >
                        Done
                        </Button>
                    </DialogActions>
                </Dialog>
            </div>
        );
    }
}

export default TaskDialog
