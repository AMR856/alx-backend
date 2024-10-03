

const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }

  for (const job of jobs) {
    const my_job = queue.create('push_notification_code_3', job);
    my_job
      .on('enqueue', () => {
        console.log('Notification job created:', my_job.id);
      })
      .on('complete', () => {
        console.log(`Notification job ${my_job.id} completed`);
      })
      .on('failed', (err) => {
        console.log(`Notification job ${my_job.id} failed: ${err}`);
      })
      .on('progress', (progress, _data) => {
        console.log('Notification job', job.id, `${progress}% complete`);
  });
  my_job.save();
  }
};

module.exports = createPushNotificationsJobs;
