import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// Initialize Express app
const app = express();
const port = 1245;

// List of products
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Get item by ID
const getItemById = (id) => {
  return listProducts.find(item => item.id === id);
};

// Initialize Redis client
const redisClient = redis.createClient();
const reserveStock = promisify(redisClient.set).bind(redisClient);
const getReservedStock = promisify(redisClient.get).bind(redisClient);

// Middleware to handle JSON responses
app.use(express.json());

// Route to get list of products
app.get('/list_products', (req, res) => {
  const products = listProducts.map(product => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock
  }));
  res.json(products);
});

// Route to get product details by itemId
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const availableQuantity = product.stock - reservedStock;

  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: availableQuantity
  });
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const availableQuantity = product.stock - reservedStock;

  if (availableQuantity < 1) {
    return res.status(400).json({
      status: 'Not enough stock available',
      itemId: product.id
    });
  }

  await reserveStock(`item.${itemId}`, reservedStock + 1);
  res.json({
    status: 'Reservation confirmed',
    itemId: product.id
  });
});

// Helper function to get current reserved stock by itemId
const getCurrentReservedStockById = async (itemId) => {
  const reserved = await getReservedStock(`item.${itemId}`);
  return reserved ? parseInt(reserved, 10) : 0;
};

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
