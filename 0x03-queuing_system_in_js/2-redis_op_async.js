import redis from 'redis';
import { promisify } from 'util';

// Create Redis client
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Sets a new value in Redis.
 * @param {string} schoolName - The key name.
 * @param {string} value - The value to set.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Promisify the client.get function
const getAsync = promisify(client.get).bind(client);

/**
 * Displays the value of a key from Redis.
 * @param {string} schoolName - The key name.
 */
async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.log(`Error: ${err}`);
  }
}

// Test the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
