import { useState, useEffect } from 'react'
import './App.css'
import Navegacion from './components/Navegacion.jsx'
import Resultados from './components/Resultados.jsx'

function App() {

  const [productos, setProductos] = useState([])
  const [ProductosFiltrados, setProductosFiltrados] = useState([])

  function cambiado(valor) {
    setProductosFiltrados(
      productos.filter((producto) =>
        producto.title.toLowerCase().includes(valor.toLowerCase())
      )
    )
  }

  useEffect(() => {
    fetch("http://localhost:8000/api/producto")
      .then((response) => response.json())
      .then((prods) => {
        setProductos(prods)
      })
  }, [])

  return (
    <div className="App">
      <Navegacion cambiado={cambiado} />
      <Resultados productos={ProductosFiltrados} />
    </div>
  )
}

export default App
