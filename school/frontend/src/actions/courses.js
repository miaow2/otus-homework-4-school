import axios from 'axios';

import { GET_COURSES, GET_ERRORS, LEAVE_COURSE } from './types';
import { getConfig } from './utils';

export const getCourses = () => (dispatch, getState) => {

  const id = getState().auth.user.id;

  axios
    .get(`/api/school/courses/?participants_id=${id}`, getConfig(getState))
    .then((res) => {
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

export const leaveCourse = (courseId, userId) => (dispatch, getState) => {

  const coursesList = getState().courses.courses

  axios
    .get(`/api/school/courses/${courseId}`, getConfig(getState))
    .then((res) => {
      const participants = res.data.participants;
      const newParticipants = participants.filter((item) => item.id !== userId);
      const data = {
        participants: newParticipants
      }
      axios.patch(`/api/school/courses/${courseId}/`, data, getConfig(getState))
        .then((res) => {
          dispatch({
            type: LEAVE_COURSE,
            payload: coursesList.filter((item) => item.id !== courseId)
          })
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