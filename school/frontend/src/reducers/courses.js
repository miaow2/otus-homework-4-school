import { GET_COURSES, FLUSH_COURSES, LEAVE_COURSE } from '../actions/types';

const initialState = {
  courses: []
};

export const courses = (state = initialState, action) => {
  switch (action.type) {
    case GET_COURSES:
      return {
        ...state,
        courses: action.payload
      };
    case LEAVE_COURSE:
      return {
        ...state,
        courses: state.courses.filter((course) => course.id !== action.payload)
      }
    case FLUSH_COURSES:
      return {
        ...state,
        courses: []
      }
    default:
      return state;
  };
};

export default courses;