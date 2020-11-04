import React, { useEffect } from 'react';
import { connect } from 'react-redux';

import { changeToken } from '../../actions/auth';
import { getCourses, flushCourses, leaveCourse } from '../../actions/courses';

const Profile = ({ auth, courses, changeToken, getCourses, flushCourses, leaveCourse }) => {

  useEffect(() => {
    getCourses();
    return () => {
      flushCourses()
    }
  }, [])

  const coursesList = (
    <table className="table table-striped">
      <thead>
        <tr>
          <th>Name</th>
          <th>Description</th>
          <th />
        </tr>
      </thead>
      <tbody>
        {courses.courses.map((item) => (
          <tr key={item.id}>
            <td>{item.name}</td>
            <td>{item.description}</td>
            <td>
              <button className="btn btn-danger btn-sm"
                onClick={() => leaveCourse(item.id, auth.user.id)}>Leave</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );

  return (
    <>
      <div className="row mt-4">
        <div className="col-md-4">
          <h3>Profile</h3>
          <div className="card card-body">
            <p><span>Username: {auth.user.username}</span></p>
          </div>
        </div>
        <div className="col-md-8">
          <h3>Token</h3>
          <div className="card card-body">
            <p className="card-text">
              Token: <samp className="mr-3">{auth.token}</samp>
              <button className="btn btn-success btn-sm mb-1"
                onClick={changeToken}>Change</button>
            </p>
          </div>
        </div>
      </div>
      <div className="row mt-4">
        <h3>Your Courses</h3>
        {coursesList}
      </div>
    </>
  )
};

const mapStateToProps = (state) => ({
  auth: state.auth,
  courses: state.courses
});

export default connect(mapStateToProps, { changeToken, getCourses, flushCourses, leaveCourse })(Profile);