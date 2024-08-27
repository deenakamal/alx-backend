import redis from 'redis';

const redisC = redis.createClient();

redisC.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

redisC.on('connect', () => {
  console.log('Redis client connected to the server');
});

function createHash() {
  redisC.hset('HolbertonSchools', 'Portland', '50', redis.print);
  redisC.hset('HolbertonSchools', 'Seattle', '80', redis.print);
  redisC.hset('HolbertonSchools', 'New York', '20', redis.print);
  redisC.hset('HolbertonSchools', 'Bogota', '20', redis.print);
  redisC.hset('HolbertonSchools', 'Cali', '40', redis.print);
  redisC.hset('HolbertonSchools', 'Paris', '2', redis.print);
}

function displayHash() {
  redisC.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.error(`Error retrieving hash: ${err.message}`);
    } else {
      console.log(reply);
    }
  });
}

createHash();
displayHash();
