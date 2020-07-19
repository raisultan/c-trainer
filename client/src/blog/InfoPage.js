import React from "react";
import {Card, PageHeader} from 'antd';
import api from '../utils/api';

export default class extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      page: {},
    }
  }

  componentDidMount() {
    const id = this.props.match.params.id;
    api.getCompressorPage(id)
      .then(res => this.setState({ page: res.data }))
  }

  render() {
    const { image, title, text } = this.state.page;
    return (
      <div>
        <PageHeader
          className="site-page-header"
          title={`/ Компрессор / ${title}`}
        />
        <Card
          style={{ width: '75%', display: 'table', margin: '0 auto' }}
          cover={<img alt={image} src={`${api.baseUrl}/media/${image}`} />}
        >
          <Card.Meta title={title} description={text} />
        </Card>
      </div>
    )
  }
}
