import React from "react";
import api from '../utils/api';
import { Card, PageHeader } from "antd";

export default class extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      list: [
        {
          "image": "compressors/shrek.jpg",
          "title": "Title lorem ipsum LOOOL",
          "text": "express: This is Express itself.\r\nhelmet: This is a library that helps to secure Express apps with various HTTP headers.\r\nmorgan: This is a library that adds some logging capabilities to your Express app.\r\nNote: As the goal of this article is to help you develop your first React application, the list above contains a very brief explanation of what each library brings to the table. You can always refer to the official web pages of these libraries to learn more about their capabilities.\r\n\r\nAfter installing these libraries, you will be able to see that NPM changed your package.json file to include them in the dependencies property. Also, you will see a new file called package-lock.json. NPM uses this file to make sure that anyone else using your project (or even yourself in other environments) will always get versions compatible with those that you are installing now.\r\n\r\nThen, the last thing you will need to do is to develop the backend source code. So, create a directory called src inside your backend directory and create a file called index.js inside this new directory. In this file, you can add the following code:"
        },
        {
          "image": "compressors/shrek.jpg",
          "title": "Title lorem ipsum LOOOL",
          "text": "express: This is Express itself.\r\nhelmet: This is a library that helps to secure Express apps with various HTTP headers.\r\nmorgan: This is a library that adds some logging capabilities to your Express app.\r\nNote: As the goal of this article is to help you develop your first React application, the list above contains a very brief explanation of what each library brings to the table. You can always refer to the official web pages of these libraries to learn more about their capabilities.\r\n\r\nAfter installing these libraries, you will be able to see that NPM changed your package.json file to include them in the dependencies property. Also, you will see a new file called package-lock.json. NPM uses this file to make sure that anyone else using your project (or even yourself in other environments) will always get versions compatible with those that you are installing now.\r\n\r\nThen, the last thing you will need to do is to develop the backend source code. So, create a directory called src inside your backend directory and create a file called index.js inside this new directory. In this file, you can add the following code:"
        },
        {
          "image": "compressors/shrek.jpg",
          "title": "Title lorem ipsum LOOOL",
          "text": "express: This is Express itself.\r\nhelmet: This is a library that helps to secure Express apps with various HTTP headers.\r\nmorgan: This is a library that adds some logging capabilities to your Express app.\r\nNote: As the goal of this article is to help you develop your first React application, the list above contains a very brief explanation of what each library brings to the table. You can always refer to the official web pages of these libraries to learn more about their capabilities.\r\n\r\nAfter installing these libraries, you will be able to see that NPM changed your package.json file to include them in the dependencies property. Also, you will see a new file called package-lock.json. NPM uses this file to make sure that anyone else using your project (or even yourself in other environments) will always get versions compatible with those that you are installing now.\r\n\r\nThen, the last thing you will need to do is to develop the backend source code. So, create a directory called src inside your backend directory and create a file called index.js inside this new directory. In this file, you can add the following code:"
        },
        {
          "image": "compressors/shrek.jpg",
          "title": "Title lorem ipsum LOOOL",
          "text": "express: This is Express itself.\r\nhelmet: This is a library that helps to secure Express apps with various HTTP headers.\r\nmorgan: This is a library that adds some logging capabilities to your Express app.\r\nNote: As the goal of this article is to help you develop your first React application, the list above contains a very brief explanation of what each library brings to the table. You can always refer to the official web pages of these libraries to learn more about their capabilities.\r\n\r\nAfter installing these libraries, you will be able to see that NPM changed your package.json file to include them in the dependencies property. Also, you will see a new file called package-lock.json. NPM uses this file to make sure that anyone else using your project (or even yourself in other environments) will always get versions compatible with those that you are installing now.\r\n\r\nThen, the last thing you will need to do is to develop the backend source code. So, create a directory called src inside your backend directory and create a file called index.js inside this new directory. In this file, you can add the following code:"
        },
        {
          "image": "compressors/shrek.jpg",
          "title": "Title lorem ipsum LOOOL",
          "text": "express: This is Express itself.\r\nhelmet: This is a library that helps to secure Express apps with various HTTP headers.\r\nmorgan: This is a library that adds some logging capabilities to your Express app.\r\nNote: As the goal of this article is to help you develop your first React application, the list above contains a very brief explanation of what each library brings to the table. You can always refer to the official web pages of these libraries to learn more about their capabilities.\r\n\r\nAfter installing these libraries, you will be able to see that NPM changed your package.json file to include them in the dependencies property. Also, you will see a new file called package-lock.json. NPM uses this file to make sure that anyone else using your project (or even yourself in other environments) will always get versions compatible with those that you are installing now.\r\n\r\nThen, the last thing you will need to do is to develop the backend source code. So, create a directory called src inside your backend directory and create a file called index.js inside this new directory. In this file, you can add the following code:"
        },
        {
          "image": "compressors/shrek.jpg",
          "title": "Title lorem ipsum LOOOL",
          "text": "express: This is Express itself.\r\nhelmet: This is a library that helps to secure Express apps with various HTTP headers.\r\nmorgan: This is a library that adds some logging capabilities to your Express app.\r\nNote: As the goal of this article is to help you develop your first React application, the list above contains a very brief explanation of what each library brings to the table. You can always refer to the official web pages of these libraries to learn more about their capabilities.\r\n\r\nAfter installing these libraries, you will be able to see that NPM changed your package.json file to include them in the dependencies property. Also, you will see a new file called package-lock.json. NPM uses this file to make sure that anyone else using your project (or even yourself in other environments) will always get versions compatible with those that you are installing now.\r\n\r\nThen, the last thing you will need to do is to develop the backend source code. So, create a directory called src inside your backend directory and create a file called index.js inside this new directory. In this file, you can add the following code:"
        },
        {
          "image": "compressors/shrek.jpg",
          "title": "Title lorem ipsum LOOOL",
          "text": "express: This is Express itself.\r\nhelmet: This is a library that helps to secure Express apps with various HTTP headers.\r\nmorgan: This is a library that adds some logging capabilities to your Express app.\r\nNote: As the goal of this article is to help you develop your first React application, the list above contains a very brief explanation of what each library brings to the table. You can always refer to the official web pages of these libraries to learn more about their capabilities.\r\n\r\nAfter installing these libraries, you will be able to see that NPM changed your package.json file to include them in the dependencies property. Also, you will see a new file called package-lock.json. NPM uses this file to make sure that anyone else using your project (or even yourself in other environments) will always get versions compatible with those that you are installing now.\r\n\r\nThen, the last thing you will need to do is to develop the backend source code. So, create a directory called src inside your backend directory and create a file called index.js inside this new directory. In this file, you can add the following code:"
        },
      ],
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
            <Card style={{ width: '360px', height: '260px', margin: '16px 16px' }}
              cover={
                <div style={{ 'height':'200px', width: '360px', overflow: 'hidden' }}>
                  <img
                    style={{ width: '100%', height: 'auto' }}
                    alt={page.image}
                    src={`https://www.dreamworks.com/storage/movies/shrek/shrek-he-digital.png`}
                  />
                </div>
              }
            >
              <Card.Meta title={page.title} />
            </Card>
        ))}
      </div>
      </div>
    );
  }
}
