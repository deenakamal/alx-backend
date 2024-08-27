import kue from 'kue';

const queue = kue.createQueue();

const blackListedPhoneNumber = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
    job.progress(0, 100);

    if (blackListedPhoneNumber.includes(phoneNumber)) {
        done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    setTimeout(() => {
        job.progress(50, 100);
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
        done();
    }, 1000);
}

queue.process('push_notification_code_2', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
