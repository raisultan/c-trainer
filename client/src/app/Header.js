import {Link} from "react-router-dom";
import React from "react";
import { Layout, Menu } from 'antd';

const { Header } = Layout;

export default () => (
  <Header>
    <div className="logo" />
    <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
      <Menu.Item key="1">
        <Link to="/home">Главная</Link>
      </Menu.Item>
      <Menu.Item key="2">
        <Link to="/training">Обучение</Link>
      </Menu.Item>
      <Menu.Item key="3">
        <Link to="/exam">Экзамен</Link>
      </Menu.Item>
    </Menu>
  </Header>
)
