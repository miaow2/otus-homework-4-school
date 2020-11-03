import { combineReducers } from 'redux';
import home from './home-reducer';
import auth from './auth-reducer';

export default combineReducers({
  auth,
  home
});