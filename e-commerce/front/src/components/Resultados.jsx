import React from 'react'

import Producto from './Producto.jsx'

export default function Resultados({ productos }) {
  return (
    <div className="d-flex flex-column mt-5">
      {
        productos.map((producto) =>
          <Producto key={producto.title} producto={producto} />
        )
      }
    </div>
  )
}
