import React, { useEffect } from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import { HashRouter as Router, Switch, Route } from 'react-router-dom';

import Contacts from '../contacts';
import CoursesList from '../courses-list'
import CoursePage from '../course-page'
import Header from '../header';
import Home from '../home';
import store from '../../store';
import { Login, Register } from '../accounts';
import PrivateRoute from '../private-route';
import { loadUser } from '../actions/auth';


const App = () => {

  useEffect(() => {
    store.dispatch(loadUser())
  }, [])

  return (
    <Provider store={ store }>
      <Router>
        <Header />
        <div className="container">
          <Switch>
            <Route path="/" component={ Home } exact />
            <Route path="/courses" component={ CoursesList } exact />
            <Route path="/courses/:id" render={ ({ match }) => {
                  const { id } = match.params
                  return <CoursePage courseId={ id } />
                }} />
            <PrivateRoute path="/contacts" component={ Contacts } />
            <Route path="/register" component={ Register } />
            <Route path="/login" component={ Login } />
          </Switch>
        </div>
      </Router>
    </Provider>
  );
};

export default App;
render(<App />, document.getElementById('root'));