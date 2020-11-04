import { GET_COURSES, LEAVE_COURSE } from '../actions/types';

const initialState = {
  courses: [],
  isLoaded: false
};

export const courses = (state = initialState, action) => {
  switch (action.type) {
    case GET_COURSES:
      return {
        ...state,
        courses: action.payload,
        isLoaded: true
      };
    case LEAVE_COURSE:
      return {
        ...state,
        courses: action.payload
      }
    default:
      return state;
  };
};

export default courses;