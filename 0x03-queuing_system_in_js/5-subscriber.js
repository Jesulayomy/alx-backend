import { createClient } from 'redis';
import redis from 'redis';

const client = createClient()
  .on('error', err => console.log('Redis client not connected to the server: Error:', err.message))
  .on('connect', () => console.log('Redis client connected to the server'));

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.quit();
  }
});
