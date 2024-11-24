import React from 'react'

import Card from 'react-bootstrap/Card';

export default function Producto({ producto }) {
  return (
    <Card className="mb-4" style={{ width: '22rem' }}>
      <Card.Img variant="top" src="" />
      <Card.Body>
        <Card.Title>{producto.title}</Card.Title>
        <Card.Text>
          {producto.description}
        </Card.Text>
        <Card.Text className="fs-4">
          💲{producto.price}
        </Card.Text>
      </Card.Body>
    </Card>
  );
}