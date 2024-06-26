const { createClient } = require('redis');

const CHANNEL_NAME = 'holberton school channel';
const client = createClient();

client.on('error', (err) => 
  console.log(`Redis client not connected to the server: ${err}`) 
);


client.on('connect', () => console.log('Redis client connected to the server'));
client.subscribe(CHANNEL_NAME);

client.on('message', (_, msg) => {
  console.log(msg);
  if (msg === 'KILL_SERVER'){
    client.unsubscribe();
    client.quit();
  }
});
