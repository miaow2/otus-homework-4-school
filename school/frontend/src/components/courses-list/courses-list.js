import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

import Spinner from '../spinner';

const CoursesList = () => {

  const [courses, setCourses] = useState([]);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    axios
      .get('/api/school/courses')
      .then((res) => {
        setCourses(res.data.results);
        setLoaded(true)
      })
      .catch((err) => console.log(err));
  }, [])

  if (courses.length === 0 & loaded) {
    return (
      <div style={{ textAlign: 'center' }}>
        <h3>There are no courses</h3>
      </div>
    );
  };

  if (loaded) {
    const items = courses.map((item) => {
      return (
        <div key={item.id} className="col-sm-3 pb-4">
          <div className="card card-body">
            <h5 className="card-title">{item.name}</h5>
            <p className="card-text">{item.description.slice(0, 40)}</p>
            <Link to={`/courses/${item.id}`} className="btn btn-primary">Look</Link>
          </div>
        </div>
      );
    });
    return (
      <>
        <h1>All Courses</h1>
        <div className="row">
          {items}
        </div>
      </>
    );
  }
  else {
    return (
      <>
        <Spinner />
      </>
    )
  }


};

export default CoursesList;