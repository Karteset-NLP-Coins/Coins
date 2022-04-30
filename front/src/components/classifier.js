import React from "react";
import Label from "./label";
import "./classifier.css";

const Classifier = (props) => {
  const { image, classifiedImage } = props;

  return (
    <React.Fragment>
      {image && <img src={image} alt="Coin" className="image" />}
      {classifiedImage && <Label classifiedImage={classifiedImage} />}
    </React.Fragment>
  );
};

export default Classifier;
