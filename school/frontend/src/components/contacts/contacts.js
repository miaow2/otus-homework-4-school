import axios from 'axios';
import React, { useState } from 'react';

const Contacts = () => {

  const [email, setEmail] = useState("");
  const [theme, setTheme] = useState("");
  const [message, setMessage] = useState("");

  const onSubmit = (e) => {

    e.preventDefault();

    const data = { email, theme, message }

    axios
      .post('/api/contacts/', data)
      .then((res) => console.log(res.data))
      .catch((err) => console.log(err));

    setEmail("");
    setTheme("");
    setMessage("");
  };

  return (
    <>
      <div className="row">
        <div className="col-md-6 col-offset-3">
          <h3 className="mt-4">Contacts</h3>
          <div className="card card-body">
            <p><span style={{ fontWeight: 'bold' }}>Phone:</span> +7 (499) 999-99-99</p>
            <p><span style={{ fontWeight: 'bold' }}>Address:</span> Moscow, Red Square, 1</p>
          </div>
        </div>
      </div>
      <div className="row">
        <div className="col-md-6 col-offset-3">
          <h3 className="mt-4">Feedback</h3>
          <div className="card card-body">
            <form onSubmit={onSubmit}>
              <div className="mb-2">
                <label>Your email:</label><br />
                <input
                  type="email"
                  name="feedback_email"
                  className="form-control"
                  placeholder="E-mail"
                  onChange={(e) => setEmail(e.target.value)}
                  value={email} />
              </div>
              <div className="mb-2">
                <label>Theme:</label><br />
                <input
                  type="text"
                  name="feedback_theme"
                  className="form-control"
                  placeholder="Theme"
                  onChange={(e) => setTheme(e.target.value)}
                  value={theme} />
              </div>
              <div className="mb-2">
                <label>Message:</label><br />
                <textarea
                  name="feedback_message"
                  className="form-control"
                  rows="5"
                  placeholder="Your message"
                  onChange={(e) => setMessage(e.target.value)}
                  value={message}>
                </textarea>
              </div>
              <button type="submit" className="btn btn-primary">Send</button>
            </form>
          </div>
        </div>
      </div>
    </>
  );
};

export default Contacts;