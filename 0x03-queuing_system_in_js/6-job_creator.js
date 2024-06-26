import { createQueue } from 'kue';

const queue = createQueue();
const data = { phoneNumber: '+2348034518615', message: ' Please verify your contact info' }
const job = queue
  .create('push_notification_code', jobData)
  .save((error) => {
    if (!error) console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', (result) => {
  console.log('Notification job completed');
});

job.on('failed', (err) => {
  console.log('Notification job failed');
});
