import express from "express";
import { createClient } from "redis";
import { promisify } from "util";

const app = express();
const client = createClient()
  .on("error", (err) =>
    console.log("Redis client not connected to the server: Error:", err.message)
  )
  .on("connect", () => console.log("Redis client connected to the server"));

const listProducts = [
  {
    id: 1,
    name: "Suitcase 250",
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: "Suitcase 450",
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: "Suitcase 650",
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: "Suitcase 1050",
    price: 550,
    stock: 5,
  },
];

function getItemById(id) {
  return listProducts.find((item) => item.id === id);
}

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock, (err, reply) => {
    console.log(reply);
  });
}

async function getCurrentReservedStockById(itemId) {
  const getItem = promisify(client.get).bind(client);
  const reservedStock = await getItem(`item.${itemId}`);
  return reservedStock;
}

const resetStocks = () => {
  return Promise.all(
    listProducts.map((item) =>
      promisify(client.SET).bind(client)(`item.${item.itemId}`, 0)
    )
  );
};

app.get("/list_products", (req, res) => {
  const responsePayload = listProducts.map((item) => {
    return {
      itemId: item.id,
      itemName: item.name,
      price: item.price,
      initialAvailableQuantity: item.stock,
    };
  });

  res.json(responsePayload);
});

app.get("/list_products/:itemId", async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.status(404).json({ status: "Product not found" });
  } else {
    const reservedStock = await getCurrentReservedStockById(itemId);
    const availableStock = item.stock - reservedStock;

    res.json({
      itemId: item.id,
      itemName: item.name,
      price: item.price,
      initialAvailableQuantity: item.stock,
      currentQuantity: availableStock,
    });
  }
});

app.get("/reserve_product/:itemId", async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.status(404).json({ status: "Product not found" });
  } else {
    const reservedStock = await getCurrentReservedStockById(itemId);
    const availableStock = item.stock - reservedStock;

    if (availableStock <= 0) {
      res.status(403).json({ status: "Not enough stock available", itemId });
    }

    reserveStockById(itemId, Number(reservedStock) + 1);

    res.json({ status: "Reservation confirmed", itemId });
  }
});

app.listen(1245, () => {
  resetStocks()
    .then(() => console.log("Cache cleared"));
});

export default app;
