import { combineReducers } from 'redux';
import auth from './auth';
import courses from './courses';
import home from './home';
import errors from './errors';
import messages from './messages';

export default combineReducers({
  auth,
  courses,
  home,
  errors,
  messages
});