import React from 'react';
import './styles.css';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import Login from './components/Login';
import CheckInOut from './components/CheckInOut';
import ViewAttendance from './components/ViewAttendance';

const App = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Login</Link>
            </li>
            <li>
              <Link to="/check-in-out">Check-In/Out</Link>
            </li>
            <li>
              <Link to="/view-attendance">View Attendance</Link>
            </li>
          </ul>
        </nav>

        <Switch>
          <Route exact path="/" component={Login} />
          <Route path="/check-in-out" component={CheckInOut} />
          <Route path="/view-attendance" component={ViewAttendance} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;

