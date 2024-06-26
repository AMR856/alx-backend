const { createClient, print } = require('redis');
const util = require('util')
const client = createClient();

client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));
client.on('connect', () => console.log('Redis client connected to the server'));

const clientSetter = util.promisify(client.set).bind(client);
const valueDisplay = util.promisify(client.get).bind(client);

const setNewSchool = async (schoolName, value) => {
  await clientSetter(schoolName, value);
  await print('Reply: OK')
};

const displaySchoolValue = async (schoolName) => {
  console.log(await valueDisplay(schoolName));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
