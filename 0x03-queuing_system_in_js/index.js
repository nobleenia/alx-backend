import express from 'express';
import { createQueue } from './queue.js';

const app = express();
const port = 3000;
const queue = createQueue();

// Endpoint to create a job
app.post('/job', (req, res) => {
  const job = queue.create('my_job', {
    title: 'Job Title'
  }).save((err) => {
    if (!err) console.log(`Job ${job.id} created`);
  });
  res.send(`Job ${job.id} created`);
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
