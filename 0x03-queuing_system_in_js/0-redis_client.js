const { createClient } = require('redis');

(async function() {
  const client = createClient();

  client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

  client.on('connect', () => {
    console.log('Redis client connected to the server');
  });

  await client.connect();

  try {
    console.log(await client.get('Holberton'));
    await client.set('HolbertonSanFrancisco', 100);
    console.log(await client.get('HolbertonSanFrancisco'));
  } catch (err) {
    console.error(`Error during Redis operations: ${err}`);
  }

  await client.disconnect();
})();