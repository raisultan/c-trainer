class AuthProvider {
  isLoggedIn() {
    const user = JSON.parse(localStorage.getItem('user'));
    return Boolean(user);
  }

  saveUser(user) {
    localStorage.setItem('user', JSON.stringify(user));
  }

  getAccessToken() {
    const user = JSON.parse(localStorage.getItem('user'));
    return user.tokens.access;
  }

  removeUser() {
    localStorage.removeItem('user');
  }
}

export default new AuthProvider();
