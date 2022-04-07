import React from 'react';
import Label from "./label";

function Classifier(props) {
  // const [labelsNames, setLabels] = useState("label 1")

  // console.log("here need to classify the picture with our models...")
  /*
    handleLabels = image =>{
      setLabels(...)
    }
    need to get the picture one by one and send to the model to get all the labels.
    the labelsName need to be an array that contains all the label related to this
    picture.
  */

  return (
    <div>
      {props.images.map(file => 
        <div>
          <img src={file} key={file} alt="pic"/> 
          <Label /> 
        </div>)}
    </div>
  )
}
 
export default Classifier;