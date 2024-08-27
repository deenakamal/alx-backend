import redis from 'redis';

redisC = redis.createClient();

redisC.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

redisC.on('connect', () => {
  console.log('Redis client connected to the server');
});
