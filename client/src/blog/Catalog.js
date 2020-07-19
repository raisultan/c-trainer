import React from "react";
import { Link } from "react-router-dom";
import api from '../utils/api';
import { Card, PageHeader } from "antd";

export default class extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      list: [],
    }
  }

  componentDidMount() {
    api.getCompressorList()
      .then(({ data }) => this.setState({ list: data }) );
  }

  render() {
    return (
      <div>
        <PageHeader
          className="site-page-header"
          title="/ Главная"
          subTitle="Список компрессоров"
        />
      <div style={{
        margin: '16px 16px',
        display: 'flex',
        'flex-flow': 'row wrap',
        'justify-content': 'flex-start',
      }}>
        {this.state.list.map((page) => (
          <Link to={`/compressor/${page.id}`}>
            <Card hoverable style={{ width: '360px', height: '260px', margin: '16px 16px' }}
              cover={
                <div style={{ 'height':'200px', width: '360px', overflow: 'hidden' }}>
                  <img
                    style={{ width: '100%', height: 'auto' }}
                    alt={page.image}
                    src={`${api.baseUrl}/media/${page.image}`}
                  />
                </div>
              }
            >
              <Card.Meta title={page.title} />
            </Card>
          </Link>
        ))}
      </div>
      </div>
    );
  }
}
