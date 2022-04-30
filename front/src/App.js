import "./App.css";
import React, { useState } from "react";

import "react-dropzone-uploader/dist/styles.css";
// import Dropzone from "react-dropzone-uploader";
import Classifier from "./components/classifier";
import CircularProgress from "@mui/material/CircularProgress";

const App = () => {
  const [loadedImage, setLoadedImage] = useState();
  const [isLoading, setIsLoading] = useState(false);
  const [displayImage, setDisplayImage] = useState();
  const [classifiedImage, setClassifiedImage] = useState("");

  // specify upload params and url for your files
  // const getUploadParams = ({ meta }) => {
  //   return { url: "https://httpbin.org/post" };
  // };

  // called every time a file's `status` changes
  // const handleChangeStatus = ({ meta, file }, status) => {
  //   /// here we load the loaded image
  //   setLoadedImage(file);
  //   console.log(status, meta, file);
  // };

  // receives array of files that are done uploading when submit button is clicked
  // const handleSubmit = (files, allFiles) => {
  //   console.log(files.map((f) => f.meta));
  //   allFiles.forEach((f) => f.remove());
  // };

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
    formData.append("file", loadedImage);
    const requestOptions = {
      method: "POST",
      body: formData,
    };

    // get file uploaded
    // send to backend
    try {
      const classifiedImage = await fetch(
        `http://localhost:3500/api`,
        requestOptions
      );
      // wait for response
      // show user the class
      const jsonRes = await classifiedImage.json();
      setClassifiedImage(jsonRes.result);
      setIsLoading((state) => !state);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="App">
      {/* <Dropzone
        getUploadParams={getUploadParams}
        onChangeStatus={handleChangeStatus}
        onSubmit={handleSubmit}
        accept="image/*,audio/*,video/*"
      /> */}

      <div className="container">
        <form>
          <div className="input-group">
            <label>Select files</label>
            <input onChange={handleInputChange} type="file" multiple />
          </div>
        </form>
        <Classifier classifiedImage={classifiedImage} image={displayImage} />
        {isLoading && <CircularProgress />}
        <button disabled={isLoading} onClick={classify}>
          Classify
        </button>
      </div>
    </div>
  );
};

export default App;
