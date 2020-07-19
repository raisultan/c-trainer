class AuthProvider {
  isLoggedIn() {
    const user = JSON.parse(localStorage.getItem('student'));
    return Boolean(user);
  }

  saveUser(user) {
    localStorage.setItem('student', JSON.stringify(user));
  }

  getAccessToken() {
    const user = JSON.parse(localStorage.getItem('student'));
    return user && user.tokens && user.tokens.access;
  }

  removeUser() {
    localStorage.removeItem('student');
  }
}

export default new AuthProvider();
