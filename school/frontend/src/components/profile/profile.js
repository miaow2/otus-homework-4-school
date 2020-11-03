import React from 'react';
import { connect } from 'react-redux';

import { changeToken } from '../../actions/auth';

const Profile = ({ auth, changeToken }) => {

  return (
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
          <p className="text-align center">
            <span className="mr-3">Token: <samp>{auth.token}</samp></span>
            <button className="btn btn-success btn-sm"
              onClick={changeToken}>Change</button>
          </p>
        </div>
      </div>
    </div>
  )
};

const mapStateToProps = (state) => ({
  auth: state.auth
})

export default connect(mapStateToProps, { changeToken })(Profile);