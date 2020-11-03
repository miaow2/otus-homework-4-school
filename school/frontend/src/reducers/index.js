import { combineReducers } from 'redux';
import auth from './auth';
import home from './home';
import errors from './errors';
import messages from './messages';

export default combineReducers({
  auth,
  home,
  errors,
  messages
});