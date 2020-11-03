import React, { Fragment, useEffect } from 'react';
import { connect } from 'react-redux';
import { withAlert } from 'react-alert';

const Alerts = ({ alert, errors, messages }) => {

  useEffect(() => {
    if (errors.msg.username) {
      alert.error(`Username: ${errors.msg.username.join()}`)
    };
    if (errors.msg.non_field_errors) {
      alert.error(errors.msg.non_field_errors.join())
    };
  }, [errors]);

  useEffect(() => {
    if (messages.loginSuccess) {
      alert.success(messages.loginSuccess)
    };
    if (messages.logoutSuccess) {
      alert.success(messages.logoutSuccess)
    };
    if (messages.passwordNotMatch) {
      alert.error(messages.passwordNotMatch)
    };
  }, [messages]);

  return <Fragment />;
};

const mapStateToProps = (state) => ({
  errors: state.errors,
  messages: state.messages
});

export default connect(mapStateToProps)(withAlert()(Alerts));