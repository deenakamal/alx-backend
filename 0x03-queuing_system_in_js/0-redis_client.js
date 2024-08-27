import redis from 'redis';

const redisC = redis.createClient();

redisC.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

redisC.on('connect', () => {
  console.log('Redis client connected to the server');
});
