import kue from 'kue';
import redis from 'redis';

const createQueue = () => {
  const queue = kue.createQueue();

  // Process jobs
  queue.process('my_job', (job, done) => {
    console.log(`Processing job ${job.id}`);
    setTimeout(() => {
      done();
    }, 1000);
  });

  return queue;
};

// Test Redis connection
const client = redis.createClient();
client.on('connect', () => {
  client.set('Holberton', 'School', redis.print);
  client.get('Holberton', (err, reply) => {
    console.log(reply); // Should print 'School'
  });
});

export { createQueue };
