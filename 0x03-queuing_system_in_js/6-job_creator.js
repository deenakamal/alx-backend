import kue from 'kue';
import redis from 'redis';

const redisClient = redis.createClient();

redisClient.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

const queue = kue.createQueue({
  redis: { 
    createClient: () => redisClient 
  }
});

const jobData = {
  phoneNumber: '123-456-7890',
  message: 'This is a test notification message'
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error(`Error creating job: ${err.message}`);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (error) => {
  console.error(`Notification job failed: ${error.message}`);
});

job.on('progress', (progress) => {
  console.log(`Notification job ${job.id} is ${progress}% complete`);
});
