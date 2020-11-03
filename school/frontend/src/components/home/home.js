import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';

import { getCoursesCount } from '../../actions/home';

class Home extends Component {

  componentDidMount() {
    this.props.getCoursesCount()
  };

  render() {

    const { coursesCount } = this.props.coursesCount

    return (
      <div className="col-sm-6 col-md-4">
        <div className="panel panel-default mt-4 mb-4">
          <ul className="list-group">
            <li className="list-group-item d-flex justify-content-between align-items-center">
              <h4 className="list-group-item-heading">
                <Link to="/courses">Courses</Link>
              </h4>
              <span className="badge badge-primary badge-pill">{coursesCount}</span>
            </li>
          </ul>
        </div>
      </div>
    );
  };
};

const mapStateToProps = (state) => ({
  coursesCount: state.home
});

export default connect(mapStateToProps, { getCoursesCount })(Home);