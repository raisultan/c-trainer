import {Route, Switch} from "react-router-dom";
import React from "react";
import Catalog from "../blog/Catalog";

const Routes = () => (
  <Switch>
    <Route path="/exam">
      <Exam />
    </Route>
    <Route path="/training">
      <Training />
    </Route>
    <Route path="/home">
      <Catalog />
    </Route>
  </Switch>
)

function Exam() {
  return <h2>Экзамен</h2>;
}

function Training() {
  return <h2>Обучение</h2>;
}

export default Routes;
