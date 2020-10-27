import React, { Component } from 'react';
import { render } from 'react-dom';

import Spinner from '../spinner';

export default class CoursesList extends Component {

  constructor(props) {
    super(props);
    this.state = {
      data: {},
      loading: true
    };
  };

  componentDidMount() {
    fetch("/api/school/courses")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loading: false
          };
        });
      });
  };

  render() {

    const { data, loading } = this.state;

    const spinner = loading ? <Spinner /> : null;
    const content = !loading ? <CoursesView data={ data } /> : null;

    return (
      <>
        <h1>All Courses</h1>
        { spinner }
        <div className="row">
          { content }
        </div>
      </>
    );
  };
};

const CoursesView = ({ data }) => {

  const { count, results } = data

  if (count === 0) {
    return (
      <div style="text-align: center;">
        <h3>There are no courses</h3>
      </div>
    )
  };

  const items = results.map((item) => {

    return (
      <div key={ item.id } className="col-sm-3" style={{ paddingBottom: 20 }}>
        <div className="card">
          <div className="card-body">
            <h5 className="card-title">{ item.name }</h5>
            <p className="card-text">{ item.text_short }</p>
            <a href={`/school/courses/${item.id}`} className="btn btn-primary">Look</a>
          </div>
        </div>
      </div>
    );
  });

  return (
    <>
      { items }
    </>
  )
}



render(<CoursesList />, document.getElementById('course_list'));