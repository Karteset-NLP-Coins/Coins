import * as imagePreccessHandler from "../handlers/imageProccessHandler.js";

export const runImageInModel = async (req, res) => {
  try {
    const image = "";
    console.log("running model");
    const result = await imagePreccessHandler.runImageInModel(image);
    console.log("Finished running");
    res.status(200).json({ result });
  } catch (error) {
    res.status(400).json({ msg: "Error running model", error });
  }
};
