import redis from 'redis';

// Create Redis client
const client = redis.createClient();

// Log messages on connection and error events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
