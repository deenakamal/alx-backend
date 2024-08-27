import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

// Create a Kue queue
const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  // Clear the queue before each test
  beforeEach((done) => {
    kue.Job.removeAll(done);
  });

  // Clear the queue after each test
  afterEach((done) => {
    kue.Job.removeAll(done);
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should create two new jobs in the queue', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Check the jobs in the queue
    setTimeout(() => {
      kue.Job.rangeByState('inactive', 0, -1, 'asc', (err, jobs) => {
        if (err) return done(err);

        try {
          expect(jobs).to.have.lengthOf(2);
          expect(jobs[0].data.phoneNumber).to.equal('4153518780');
          expect(jobs[0].data.message).to.equal('This is the code 1234 to verify your account');
          expect(jobs[1].data.phoneNumber).to.equal('4153518781');
          expect(jobs[1].data.message).to.equal('This is the code 5678 to verify your account');
          done();
        } catch (error) {
          done(error);
        }
      });
    }, 1000); // Allow some time for jobs to be added to the queue
  });
});
