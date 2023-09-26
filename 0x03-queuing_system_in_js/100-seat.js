import { createClient } from "redis";
import { promisify } from "util";
import { createQueue } from "kue";
import express from "express";

const client = createClient();
const finder = promisify(client.get).bind(client);
const queue = createQueue();
const app = express();


function reserveSeat(number) {
  client.set("available_seats", number, (err, reply) => {
    if (err) console.log(err);
    console.log(reply);
  });
}

async function getCurrentAvailableSeats() {
  const availableSeats = await finder("available_seats");
  return availableSeats;
}

let reservationEnabled = true;


app.get("/available_seats", async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get("/reserve_seat", async (req, res) => {
  if (!reservationEnabled)
    return res.json({ status: "Reservation are blocked" });

  const job = queue.create("reserve_seat", {}).save((err) => {
    if (err) {
      res.json({ status: "Reservation failed" });
    } else {
      res.json({ status: "Reservation in process" });
    }
  });

  job
    .on("complete", () => {
      console.log(`Seat reservation job ${job.id} completed`);
    })
    .on("failed", (err) => {
      console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });
});

app.get("/process", async (req, res) => {
  queue.process("reserve_seat", async (job, done) => {
    let availableSeats = await getCurrentAvailableSeats();
    if (availableSeats <= 0) done(Error("Not enough seats available"));
    availableSeats -= 1;
    reserveSeat(availableSeats);
    if (availableSeats === 0) reservationEnabled = false;
    done();
  });
  res.json({ status: "Queue processing" });
});

app.listen(1245);

export default app;
