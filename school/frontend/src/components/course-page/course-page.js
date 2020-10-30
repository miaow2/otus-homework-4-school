import axios from 'axios';
import React, { useEffect, useState } from 'react';

const CoursePage = ({ courseId }) => {

  const [course, setCourse] = useState({})
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    axios
    .get(`/api/school/courses/${courseId}`)
    .then((res) => {
      setCourse(res.data);
      setLoaded(true);
    })
    .catch((err) => console.log(err));
  }, [])

  return (
    <>
      <h1>{ course.name }</h1>
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
                  <td>{ course.description }</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </>
  );
};

export default CoursePage;