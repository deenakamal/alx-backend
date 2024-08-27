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

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});

console.log('Job processor is listening for jobs...');
