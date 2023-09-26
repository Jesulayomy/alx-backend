import { createQueue } from 'kue';

const queue = createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
}).save( function(err) {
  if( !err ) console.log( job.id );
});

job.on('complete', () => console.log(`Notification job ${job.id} completed`))
  .on('failed', (err) => console.log(`Notification job failed: ${err}`));
