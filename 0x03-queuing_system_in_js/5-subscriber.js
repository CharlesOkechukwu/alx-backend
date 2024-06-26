import { createClient } from 'redis';

const client = createClient();
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const response = (msg) => console.log(msg);
client.SUBSCRIBE('holberton school channel');
client.on('message', (channel, message) => {
  if (channel === 'holberton school channel') {
    if (message === 'KILL_SERVER') {
      client.UNSUBSCRIBE();
      client.QUIT();
    }
    response(message);
  }
});
