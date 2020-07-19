import {Route, Switch } from "react-router-dom";
import React from "react";
import PrivateRoute from "../auth/PrivateRoute";
import Catalog from "../blog/Catalog";
import InfoPage from "../blog/InfoPage";
import LoginForm from "../auth/LoginForm";
import Logout from "../auth/Logout";

const Routes = () => (
  <Switch>
    <PrivateRoute exact path="/exam" component={Exam} />
    <PrivateRoute exact path="/training" component={Exam} />
    <PrivateRoute exact path="/home" component={Catalog} />
    <PrivateRoute path="/compressor/:id" component={InfoPage} />
    <Route path="/logout" render={(props) => <Logout {...props} />} />
    <Route path="/login" render={(props) => <LoginForm {...props} />} />
  </Switch>
)

function Exam() {
  return <h2>Экзамен</h2>;
}

function Training() {
  return <h2>Обучение</h2>;
}

export default Routes;
