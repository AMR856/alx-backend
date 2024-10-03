import { createQueue } from 'kue';
const queue = createQueue();

const blacklist_numbers = ['4153518780', '4153518781'];


const sendNotification = (phoneNumber, message, job, done) => {
  const total = 2;
  let onProgress = 2;
  let sendInterval = setInterval(() => {
    if (total - onProgress <= total / 2){
      job.progress(total - onProgress, total);
    }
    if (blacklist_numbers.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendInterval);
      return;
    }
    if (total === onProgress) {
      console.log(`Log to the console Sending notification to ${phoneNumber}, with message: ${message}`);
    }
    --onProgress || done();
    onProgress || clearInterval(sendInterval);
  }, 1000);
};

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
