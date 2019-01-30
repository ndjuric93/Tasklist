import React from 'react';
import PropTypes from 'prop-types';
import { AppBar, Toolbar, Typography, withStyles } from '@material-ui/core';

const styles = {
    appBar: {
        alignItems: 'center',
      }
};

function TaskToolbar(props) {
    const {classes} = props
    return (
        <AppBar
            position='absolute'
            color="primary"
            className={classes.appBar}
        >
            <Toolbar>
                <Typography 
                    variant="display1" 
                    color="inherit"
                    style={{ align: "center" }}
                    >
                    TASKS
                </Typography>
            </Toolbar>
        </AppBar>
    )
}

TaskToolbar.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(TaskToolbar)