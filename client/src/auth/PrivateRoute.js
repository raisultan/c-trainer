import React from "react";
import { Redirect, Route } from 'react-router-dom';
import AuthProvider from "./authProvider";

export default function ({ component: Component, ...rest }) {
  return (
    <Route
      {...rest}
      render={(props) =>
        AuthProvider.isLoggedIn() ? (
          <Component {...props} />
        ) : (
          <Redirect
            to={{
              pathname: "/login",
              state: { from: props.location }
            }}
          />
        )
      }
    />
  );
}
