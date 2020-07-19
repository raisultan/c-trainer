import React from "react";
import { Form, Input, Button } from 'antd';
import api from '../utils/api';
import authProvider from "./authProvider";

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 7 },
};
const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

export default class extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      user: {login: '', password: ''},
      errorMessage: '',
    }
  }

  onFinish = values => {
    api.login(values.username, values.password)
      .then(({ data }) => {
        authProvider.saveUser(data);
        this.props.history.push('/home')
      })
      .catch((err) => (
        this.setState({ errorMessage: (err.response && err.response.data.detail) || 'Неверные данные' })
      ));
  };

  render() {
    return (
      <Form
        {...layout}
        name="basic"
        initialValues={{
          remember: true,
        }}
        onFinish={this.onFinish}
        style={{ marginTop: '200px' }}
      >
        {this.state.errorMessage && (
          <Form.Item>{this.state.errorMessage}</Form.Item>
        )}
        <Form.Item
          label="Логин"
          name="username"
          value={this.state.user.login}
          rules={[
            {
              required: true,
              message: 'Введите логин!',
            },
          ]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          label="Пароль"
          name="password"
          value={this.state.user.password}
          rules={[
            {
              required: true,
              message: 'Введите пароль!',
            },
          ]}
        >
          <Input.Password />
        </Form.Item>

        <Form.Item {...tailLayout}>
          <Button type="primary" htmlType="submit">
            Войти
          </Button>
        </Form.Item>
      </Form>
    )
  }
}
