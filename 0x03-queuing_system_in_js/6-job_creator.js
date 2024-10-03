const kue = require('kue'); 
const queue = kue.createQueue({'name': 'push_notification_code'});


const jobObject = {
  'phoneNumber': '01123759955',
  'message': 'Please, call me'
};

const job = queue.create('object_thing', jobObject);

job.on('enqueue', function(){
  console.log(`Notification job created: ${job.id}`);

}).on('complete', function(){
  console.log('Notification job completed');

}).on('failed', function(){
  console.log('Notification job failed');
});
job.save();