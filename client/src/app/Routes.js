import {Route, Switch} from "react-router-dom";
import React from "react";

const Routes = () => (
  <Switch>
    <Route path="/exam">
      <Exam />
    </Route>
    <Route path="/training">
      <Training />
    </Route>
    <Route path="/home">
      <Home />
    </Route>
  </Switch>
)

function Home() {
  return <h2>Главнвая</h2>;
}

function Exam() {
  return <h2>Экзамен</h2>;
}

function Training() {
  return <h2>Обучение</h2>;
}

export default Routes;
