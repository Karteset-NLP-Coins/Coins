export const runImageInModel = async (image) => {
  // run model and wait for model to finish
  // return result
  console.log("in handler");
  //  this is to resemble a model running, running 1 second
  await delay(1000);
  return "dog";
};

const delay = (ms) => {
  return new Promise((resolve) => setTimeout(resolve, ms));
};
