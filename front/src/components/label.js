import React from "react";

const Label = (props) => {
  const { classifiedImage } = props;

  const styles = {
    fontSize: 18,
    fontWeight: "bold",
  };

  return (
    <div>
      <span style={styles} className="badge m-2 bg-primary">
        {classifiedImage}
      </span>
    </div>
  );
};

export default Label;
