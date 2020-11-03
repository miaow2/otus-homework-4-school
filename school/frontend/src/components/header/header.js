import React from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';

import { logoutUser } from '../../actions/auth';

import './header.css';

const Header = ({ auth, logoutUser }) => {

  const { isAuthenticated, user } = auth

  const authLinks = (
    <>
      <li className="nav-item">
        {/* <a className="nav-link" href="#">Hello {user.username}</a> */}
        <span className="navbar-text">
          <strong>
            {user ? `Hello ${user.username}` : ""}
          </strong>
        </span>
      </li>
      <li className="nav-item">
        <button className="button-link" onClick={logoutUser}>Logout</button>
      </li>
    </>
  );

  const guestLinks = (
    <>
      <li className="nav-item">
        <Link to="/register" className="nav-link">Register</Link>
      </li>
      <li className="nav-item">
        <Link to="/login" className="nav-link">Login</Link>
      </li>
    </>
  );

  return (
    <nav className="navbar navbar-expand-lg navbar-light" style={{ background: 'bisque' }}>
      <div className="container">
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item active">
              <Link to="/" className="navbar-brand">Home</Link>
            </li>
            <li className="nav-item">
              <Link to="/courses" className="nav-link">Courses</Link>
            </li>
          </ul>
          <ul className="navbar-nav navbar-right">
            <li className="nav-item">
              <a className="nav-link" href="/graphql">GraphQL</a>
            </li>
            <li className="nav-item">
              <Link to="/contacts" className="nav-link mr-3">Contacts</Link>
            </li>
            {isAuthenticated ? authLinks : guestLinks}
          </ul>
        </div>
      </div>
    </nav>
  );
};

const mapStateToProps = (state) => ({
  auth: state.auth
});

export default connect(mapStateToProps, { logoutUser })(Header);