import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import Contacts from '../contacts';
import CoursesList from '../courses-list'
import CoursePage from '../course-page'
import Header from '../header';
import Home from '../home';
import store from '../../store';

const App = () => {

  return (
    <>
      <Provider store={ store }>
        <BrowserRouter>
          <Header />
          <div className="container">
            <Switch>
              <Route path="/" component={ Home } exact />
              <Route path="/courses" component={ CoursesList } exact />
              <Route path="/courses/:id" render={ ({ match }) => {
                    const { id } = match.params
                    return <CoursePage courseId={ id } />
                  }} />
              <Route path="/contacts" component={ Contacts } />
            </Switch>
          </div>
        </BrowserRouter>
      </Provider>
    </>
  );
};

export default App;
render(<App />, document.getElementById('root'));