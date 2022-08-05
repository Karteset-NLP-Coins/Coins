import "./App.css";
import React, { useState } from "react";

import "react-dropzone-uploader/dist/styles.css";
import Classifier from "./components/classifier";
import CircularProgress from "@mui/material/CircularProgress";

const App = () => {
  const [loadedImage, setLoadedImage] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [displayImage, setDisplayImage] = useState(null);
  const [classifiedImage, setClassifiedImage] = useState("");

  const handleInputChange = (event) => {
    setLoadedImage(event.target.files[0]);
    setDisplayImage(URL.createObjectURL(event.target.files[0]));
  };
  const classify = async (e) => {
    setClassifiedImage("");
    setIsLoading((state) => !state);
    e.preventDefault();
    // we sent post request to backend
    if (!loadedImage) {
      alert("Please upload an image");
      return;
    }
    const formData = new FormData();
    formData.append("image", loadedImage);
    const requestOptions = {
      method: "POST",
      body: formData,
    };
    // get file uploaded
    // send to backend
    try {
      const classifiedImage = await fetch(
        `http://localhost:3500/api/predict-leaves-or-thorns`,
        requestOptions
      );
      // wait for response
      // show user the class
      const jsonRes = await classifiedImage.json();
      setClassifiedImage(jsonRes.result);
    } catch (error) {
      setClassifiedImage("Failed");
      console.log(error);
    }
    setIsLoading((state) => !state);
  };

  return (
    <div className="App">
      <div className="container">
        <form>
          <div className="input-group">
            <label>Select files</label>
            <input onChange={handleInputChange} type="file" multiple />
          </div>
        </form>
        <Classifier classifiedImage={classifiedImage} image={displayImage} />
        {isLoading && <CircularProgress />}
        <button disabled={isLoading || !displayImage} onClick={classify}>
          Classify
        </button>
      </div>
    </div>
  );
};

export default App;
