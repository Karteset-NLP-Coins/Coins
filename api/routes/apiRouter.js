import express from "express";
const router = express.Router();
import upload from "../upload-manager/mutlerController.js";

import * as imageProccessController from "../controllers/imageProccessController.js";

router.post(
  "/",
  upload.single("file"),
  imageProccessController.runImageInModel
);

export default router;
