import React from "react";
import { Button } from 'antd';
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

  onFinish = () => {
    authProvider.removeUser();
    this.props.history.push('/login');
  };

  render() {
    return (
      <div>
        <Button type="primary" htmlType="submit" onClick={this.onFinish}>
          Выйти из системы
        </Button>
      </div>
    )
  }
}
