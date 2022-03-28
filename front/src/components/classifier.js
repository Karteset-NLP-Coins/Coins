import React, { Component } from 'react';
import Label from ".//label";
import h from '../images/h.png'
import a from '../images/a.jpg'

class Classifier extends Component {
    state = {  } 
    render() { 
        return (
          <div>
            <img src={h} alt="pic1" height={200} width={350}/>
            <Label />
            <br />
            <br />
            <img src="https://knowledge.wharton.upenn.edu/wp-content/uploads/2016/04/network-connections.jpg"
            alt="pic2" height={200} width={350} />
            <Label />
            <br />
            <img src={a}
            alt="pic3" height={200} width={350} />
            <Label />
          </div>
        );
    }
}
 
export default Classifier;