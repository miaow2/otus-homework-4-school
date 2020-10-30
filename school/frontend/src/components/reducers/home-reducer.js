import { COURSE_COUNT } from '../actions/types';

const initialState = {
  home: {
    coursesCount: 0
  }
};

const home = (state = initialState, action) => {
  switch (action.type) {
    case COURSE_COUNT:
      return {
        ...state,
        home: {
          coursesCount: action.payload
        }
      }
    default:
      return state
  };
};

export default home;