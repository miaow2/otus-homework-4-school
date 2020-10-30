import React from 'react';
import { Link } from 'react-router-dom';

import './header.css';

const Header = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light" style={{ background: 'bisque' }}>
      <div className="container">
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item active">
              <Link to="/">Home</Link>
            </li>
            <li className="nav-item active">
              <Link to="/courses">Courses</Link>
            </li>
          </ul>
          <ul className="navbar-nav navbar-right">
            <li className="nav-item active">
              <a className="nav-link" href="/graphql">GraphQL</a>
            </li>
            <li className="nav-item active">
              <Link to="/contacts">Contacts</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Header;