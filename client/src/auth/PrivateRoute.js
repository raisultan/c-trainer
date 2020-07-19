import React from "react";
import { Redirect, Route } from 'react-router-dom';
import AuthProvider from "./authProvider";

export default function ({ children, ...rest }) {
  return (
    <Route
      {...rest}
      render={({ location }) =>
        AuthProvider.isLoggedIn() ? (
          children
        ) : (
          <Redirect
            to={{
              pathname: "/login",
              state: { from: location }
            }}
          />
        )
      }
    />
  );
}
