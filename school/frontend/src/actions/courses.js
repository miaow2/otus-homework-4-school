import axios from 'axios';

import { createMessage } from './messages';
import {
  GET_COURSES,
  GET_ERRORS,
  FLUSH_COURSES,
  LEAVE_COURSE
} from './types';
import { getConfig } from './utils';

export const getCourses = () => (dispatch, getState) => {

  const id = getState().auth.user.id;

  axios
    .get(`/api/courses/?participants_id=${id}`, getConfig(getState))
    .then((res) => {
      console.log(res.data)
      console.log(res.url)
      dispatch({
        type: GET_COURSES,
        payload: res.data.results,
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
    });
};

export const leaveCourse = (courseId) => (dispatch, getState) => {

  const data = {
    course_id: courseId
  };

  axios
    .post("/api/courses/leave", data, getConfig(getState))
    .then((res) => {
      dispatch(createMessage({
        leaveCourse: "Leave from course"
      }));
      dispatch({
        type: LEAVE_COURSE,
        payload: courseId
      })
    })
    .catch((err) => {
      console.log(err)
      const errors = {
        msg: err.response.data,
        status: err.response.status
      };
      dispatch({
        type: GET_ERRORS,
        payload: errors
      });
    });
};

export const enrollCourse = (courseId) => (dispatch, getState) => {

  const data = {
    course_id: courseId
  };

  axios
    .post("/api/courses/enroll", data, getConfig(getState))
    .then((res) => {
      dispatch(createMessage({
        enrollCourse: "Enroll in course"
      }));
      getCourses();
    })
    .catch((err) => {
      console.log(err)
      const errors = {
        msg: err.response.data,
        status: err.response.status
      };
      dispatch({
        type: GET_ERRORS,
        payload: errors
      });
    });
};

export const flushCourses = () => (dispatch) => {

  dispatch({
    type: FLUSH_COURSES
  })
};