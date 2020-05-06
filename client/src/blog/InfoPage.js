import React from "react";
import {Card, PageHeader} from 'antd';

export default ({ image, title, text }) => (
  <div>
    <PageHeader
      className="site-page-header"
      title={`/Главная/${title}`}
      subTitle="Список компрессоров"
    />
    <Card
      // style={{ width: 240 }}
      cover={<img alt={image} src={`localhost:8000/api/media/${image}`} />}
    >
      <Card.Meta title={title} description={text} />
    </Card>
  </div>
)
