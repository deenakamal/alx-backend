import redis from 'redis';
import { promisify } from 'util';

const redisC = redis.createClient();

redisC.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

redisC.on('connect', () => {
  console.log('Redis client connected to the server');
});

const getAsync = promisify(redisC.get).bind(redisC);

function setNewSchool(schoolName, value) {
  redisC.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
