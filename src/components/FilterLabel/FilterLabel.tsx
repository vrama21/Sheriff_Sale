import { InputLabel } from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';

export const FilterLabel = withStyles((theme) => ({
  root: {
    color: 'white',
    fontWeight: 'bold',
    paddingLeft: '0.5rem',
    position: 'absolute',
    zIndex: 1,
  },
  focused: {
    color: theme.palette.primary.light,
  },
}))(InputLabel);
