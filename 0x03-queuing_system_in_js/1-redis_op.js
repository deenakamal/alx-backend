import redis from 'redis';

const redisC = redis.createClient();

redisC.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

redisC.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  redisC.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  redisC.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
    } else {
      console.log(reply);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
