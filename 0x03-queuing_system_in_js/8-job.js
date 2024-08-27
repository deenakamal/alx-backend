import kue from 'kue';

const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData)
      .on('enqueue', (id) => {
        console.log(`Notification job created: ${id}`);
      })
      .on('complete', (id) => {
        console.log(`Notification job ${id} completed`);
      })
      .on('failed', (id, errorMessage) => {
        console.log(`Notification job ${id} failed: ${errorMessage}`);
      })
      .on('progress', (id, progress) => {
        console.log(`Notification job ${id} ${progress}% complete`);
      });

    job.save();
  });
};

export default createPushNotificationsJobs;
