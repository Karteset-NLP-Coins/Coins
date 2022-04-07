import "./App.css";
import { useState } from "react";
import "react-dropzone-uploader/dist/styles.css";
import Dropzone from "react-dropzone-uploader";
import Classifier from "./components/classifier";

const App = () => {
 const [images, setImages] = useState([]);

  // specify upload params and url for your files
  const getUploadParams = ({ meta }) => {
    return { url: "https://httpbin.org/post" };
  };

  // called every time a file's `status` changes
  const handleChangeStatus = ({ meta, file }, status) => {
    // console.log(status, meta, file);
  };

  // receives array of files that are done uploading when submit button is clicked
  const handleSubmit = (files, allFiles) => {
    // console.log(files.map(f => f.meta));   
    allFiles.forEach(f => f.remove());

    files.forEach(file => {
      let reader = new FileReader();
      reader.onload = e => {
        const dateUrl = e.target.result;
        images.push(dateUrl);
        setImages([...images]);
      };
      reader.readAsDataURL(file.file);
    })

    // reader.readAsDataURL(files[0].file); // loop all the picture
  };

  return (
    <div className="App">
      <Dropzone
        multiple={true}
        getUploadParams={getUploadParams}
        onChangeStatus={handleChangeStatus}
        onSubmit={handleSubmit}
        accept="image/*"
      />   
      <Classifier images={images}/>
    </div>
  );
};

export default App;