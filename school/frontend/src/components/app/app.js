import React, { Component } from 'react';
import { render } from 'react-dom';

export default class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      data: {},
      loaded: false,
      placeholder: "Loading"
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
            loaded: true
          };
        });
      });
  };

  render() {
    return (
      <div className="col-sm-6 col-md-4">
        <div className="panel panel-default">
            <ul className="list-group">
              <li className="list-group-item d-flex justify-content-between align-items-center">
                <h4 className="list-group-item-heading"><a href="school/courses">Courses</a></h4>
                <span className="badge badge-primary badge-pill">{ this.state.data.count }</span>
              </li>
            </ul>
        </div>
      </div>
    );
  };
};

render(<App />, document.getElementById('home'));