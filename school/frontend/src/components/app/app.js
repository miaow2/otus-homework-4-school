import React, { Fragment, useEffect } from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Provider as AlertProvider } from 'react-alert';
import AlertTemplate from 'react-alert-template-basic';

import Alerts from '../alerts';
import Contacts from '../contacts';
import CoursesList from '../courses-list'
import CoursePage from '../course-page'
import Header from '../header';
import Home from '../home';
import store from '../../store';
import PrivateRoute from '../private-route';
import Profile from '../profile';
import { Login, Register } from '../accounts';
import { loadUser } from '../../actions/auth';

const alertOptions = {
  timeout: 5000,
  position: "top center"
};

const App = () => {

  useEffect(() => {
    store.dispatch(loadUser())
  }, [])

  return (
    <Provider store={store}>
      <AlertProvider template={AlertTemplate} {...alertOptions}>
        <Router>
          <Header />
          <Alerts />
          <div className="container">
            <Switch>
              <Route path="/" component={Home} exact />
              <Route path="/courses" component={CoursesList} exact />
              <Route path="/courses/:id" render={({ match }) => {
                const { id } = match.params
                return <CoursePage courseId={id} />
              }} />
              <Route path="/contacts" component={Contacts} />
              <Route path="/register" component={Register} />
              <Route path="/login" component={Login} />
              <PrivateRoute path="/profile" component={Profile} />
            </Switch>
          </div>
        </Router>
      </AlertProvider>
    </Provider>
  );
};

export default App;
render(<App />, document.getElementById('root'));