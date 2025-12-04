const jsonServer = require('json-server')
const server = jsonServer.create()
const router = jsonServer.router('db.json')
const middlewares = jsonServer.defaults()

server.use(middlewares)
server.use(router)

const port = process.env.PORT || 3000
server.listen(port, () => {
  console.log('MyStore API running on port', port)
  console.log('Products:   http://localhost:' + port + '/products')
  console.log('Users:      http://localhost:' + port + '/users')
  console.log('Carts:      http://localhost:' + port + '/carts')
  console.log('Orders:     http://localhost:' + port + '/orders')
})
