import { Client } from "discord.js";
import { config } from "dotenv";

// Bot token setup, reads from .env file
config();
const TOKEN: string = process.env.BOT_TOKEN;
// console.log(TOKEN);

const client: Client = new Client({
    intents: []
});

client.login(TOKEN);
