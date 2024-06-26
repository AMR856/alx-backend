const { createClient, print } = require('redis');
const client = createClient();

const HASH_KEY = 'HolbertonSchools';
client.on('connect', () => {
  console.log('Redis client connected to the server');
  mainFunction()
});

client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));


function addHash(key, value){
  client.hset(HASH_KEY, key, value, () => {
    print('Reply: 1');
  });
}

function printHash(key) {
  client.hgetall(key, (_, reply) => {
    console.log(reply);
  });
}

function mainFunction() {
  const myHashes = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2
  };
  for (const [key, value] of Object.entries(myHashes)) {
    addHash(key, value);
  }
  printHash(HASH_KEY);
}
