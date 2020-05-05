import React from "react";
import { Card } from 'antd';

export default ({ image, title, text }) => (
  <div>
    <Card
      // style={{ width: 240 }}
      cover={<img alt={image} src={`localhost:8000/api/media/${image}`} />}
    >
      <Card.Meta title={title} description={text} />
    </Card>
  </div>
)
