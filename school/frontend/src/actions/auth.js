import axios from 'axios';

import { createMessage } from './messages'
import {
  USER_LOADING,
  USER_LOADED,
  AUTH_ERROR,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT_SUCCESS,
  REGISTER_FAIL,
  REGISTER_SUCCESS,
  GET_ERRORS
} from './types';

export const loadUser = () => (dispatch, getState) => {

  dispatch({
    type: USER_LOADING
  });

  const token = getState().auth.token;

  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  if (token) {
    config.headers["Authorization"] = `Token ${token}`;
  };

  axios
    .get('/api/auth/user', config)
    .then((res) => {
      dispatch({
        type: USER_LOADED,
        payload: res.data,
      });
    })
    .catch((err) => {
      dispatch({
        type: AUTH_ERROR
      })
    });
};

export const loginUser = (username, password) => (dispatch) => {

  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  const body = JSON.stringify({ username, password })

  axios
    .post('/api/auth/login', body, config)
    .then((res) => {
      dispatch(createMessage({
        loginSuccess: "Login Successful"
      }));
      dispatch({
        type: LOGIN_SUCCESS,
        payload: res.data,
      });
    })
    .catch((err) => {
      const errors = {
        msg: err.response.data,
        status: err.response.status
      };
      dispatch({
        type: GET_ERRORS,
        payload: errors
      });
      dispatch({
        type: LOGIN_FAIL
      });
    });
};

export const registerUser = (username, password) => (dispatch) => {

  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  const body = JSON.stringify({ username, password })

  axios
    .post('/api/auth/register', body, config)
    .then((res) => {
      dispatch({
        type: REGISTER_SUCCESS,
        payload: res.data,
      });
    })
    .catch((err) => {
      const errors = {
        msg: err.response.data,
        status: err.response.status
      };
      dispatch({
        type: GET_ERRORS,
        payload: errors
      });
      dispatch({
        type: REGISTER_FAIL
      })
    });
};

export const logoutUser = () => (dispatch) => {

  dispatch(createMessage({
    logoutSuccess: "Logout Successful"
  }));

  dispatch({
    type: LOGOUT_SUCCESS
  });
};