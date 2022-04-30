import express from "express";
const app = express();
import dotenv from "dotenv";
dotenv.config();
import cors from "cors";

import apiRouter from "./routes/apiRouter.js";

app.use(express.json());
app.use(cors());
app.use("/api", apiRouter);

const port = process.env.PORT || 3000;

const startServer = () => {
  // connect to mongo here

  app.listen(port, () => {
    console.log(`running server on port ${port} `);
  });
};

startServer();
