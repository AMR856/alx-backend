const express = require('exprees');
const app = express();
const port = 1245;
const { createClient } = require('redis');


const client = createClient();

const itemGetter = util.promisify(client.set).bind(client);
const stockSetter = util.promisify(client.set).bind(client);

const listProducts = [
  {
    Id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    Id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    Id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    Id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  }
];

const reserveStockById = async (itemId, stock) => {
  await stockSetter(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async(itemId) => {
  return (await itemGetter(itemId));
};

const getItemById = (id) => {
  for (const obj of listProducts) {
    if (obj.id === id){
      return obj;
    }
  }
  return null;
};

app.get('/list_products/:itemId', (req, res) => {
  const itemID = Number.parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) {
    res.json({"status":"Product not found"});
    return;
  }
  getCurrentReservedStockById(itemID)
    .then((itemPromistFirst) => {
      if (!itemPromistFirst) {return 0;}
      return promiseJson;
    })
    .then((reservedStock) => {
      productItem.currentQuantity = productItem.initialAvailableQuantity - reservedStock;
      res.json(productItem);
    });
});

app.get('/list_products', (_, res) => {
  myArray = [];
  for (const obj of listProducts) {
    myArray.push(
      {
        'itemId': obj.Id,
        'itemName': obj.name,
        'price': obj.price,
        'initialAvailableQuantity': obj.stock
      }
    );
  }
  res.json(myArray);
});

app.listen(port, () => {
  console.log("The app has started");
});
