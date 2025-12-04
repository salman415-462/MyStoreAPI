const jsonServer = require('json-server');
const server = jsonServer.create();
const router = jsonServer.router('db.json');
const middlewares = jsonServer.defaults();

// Set default middlewares (logger, static, cors)
server.use(middlewares);

// To handle POST, PUT and PATCH you need to use a body-parser
server.use(jsonServer.bodyParser);

// Use default router
server.use(router);

const port = process.env.PORT || 3000;
server.listen(port, () => {
  console.log(`🚀 MyStore API Server is running on port ${port}`);
  console.log(`📊 Endpoints:`);
  console.log(`   http://localhost:${port}/products`);
  console.log(`   http://localhost:${port}/users`);
  console.log(`   http://localhost:${port}/carts`);
  console.log(`   http://localhost:${port}/orders`);
  console.log(`\n📝 Try: curl http://localhost:${port}/products`);
});
