import dotenv from "dotenv";
import express from "express";
import TelegramBot from "node-telegram-bot-api";

dotenv.config();

const token = process.env.TOKEN;
const port: string | number = process.env.PORT ?? 1234;

const app = express();
const bot = new TelegramBot(token!, { polling: true });

app.use(express.json());

app.listen(port, () => {
  console.log(`Express server is listening on ${port}`);
});

// Just to ping!
bot.on("message", (msg) => {
  bot.sendMessage(msg.chat.id, "I am alive!");
});
