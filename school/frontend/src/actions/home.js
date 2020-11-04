import axios from 'axios';

import { COURSE_COUNT } from './types';

export const getCoursesCount = () => (dispatch) => {
  axios
    .get('/api/courses')
    .then((res) => {
      dispatch({
        type: COURSE_COUNT,
        payload: res.data.count,
      });
    })
    .catch((err) => console.log(err));
};