import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { connect } from 'react-redux';

import Spinner from '../spinner';
import { enrollCourse, leaveCourse } from '../../actions/courses';

const CoursePage = ({ courseId, auth, enrollCourse, leaveCourse }) => {

  const [course, setCourse] = useState({})
  const [loaded, setLoaded] = useState(false);

  const getCourse = () => {
    axios
      .get(`/api/courses/${courseId}`)
      .then((res) => {
        setCourse(res.data);
        setLoaded(true);
      })
      .catch((err) => console.log(err));
  };

  useEffect(() => {
    getCourse()
  }, [])

  let buttons = null

  if (loaded) {
    if (auth.isAuthenticated) {
      const participants = course.participants.map((item) => item.id)
      if (participants.includes(auth.user.id)) {
        buttons = (
          <div className="float-right mt-4">
            <button className="btn btn-danger btn-sm"
              onClick={() => {
                leaveCourse(course.id);
                setLoaded(false);
                getCourse();
              }}>Leave</button>
          </div>
        );
      } else {
        buttons = (
          <div className="float-right mt-4">
            <button className="btn btn-success btn-sm"
              onClick={() => {
                enrollCourse(course.id);
                setLoaded(false);
                getCourse();
              }}>Enroll</button>
          </div>
        );
      };
    };
  } else {
    return <Spinner />
  };

  return (
    <>
      {buttons}
      <h1>{course.name}</h1>
      <div className="row mt-4">
        <div className="col-md-6">
          <div className="card mb-4">
            <div className="card-header">
              <strong>Info</strong>
            </div>
            <table className="table table-hover card-body attr-table">
              <tbody>
                <tr>
                  <td>Description</td>
                  <td>{course.description}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </>
  );
};

const mapPropsToState = (state) => ({
  auth: state.auth
});

export default connect(mapPropsToState, { enrollCourse, leaveCourse })(CoursePage);