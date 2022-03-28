import React, { Component } from 'react';

class Label extends Component {
    state = {
        color: ['primary',
        'secondary', // mybe to delete because this is white
        'success',
        'danger',
        'warning text-dark',
        'info text-dark',
        'light text-dark',
        'dark']
    }

    styles = {
        fontSize: 18,
        fontWeight: 'bold'
    };

    render() { 
        return ( 
          <div>
            <span style={this.styles} className={this.getBadgeColor(0)}>blue</span>
            <span style={this.styles} className={this.getBadgeColor(1)}>gray</span>
            <span style={this.styles} className={this.getBadgeColor(2)}>green</span>
            <span style={this.styles} className={this.getBadgeColor(3)}>red</span>
            <span style={this.styles} className={this.getBadgeColor(4)}>yellow</span>
            <span style={this.styles} className={this.getBadgeColor(5)}>azure</span>
            <span style={this.styles} className={this.getBadgeColor(6)}>white</span>
            <span style={this.styles} className={this.getBadgeColor(7)}>black</span>
          </div>
        );
    }

    getBadgeColor(num) {
        let nameClass = 'badge m-2 bg-'
        nameClass += this.state.color[num];
        return nameClass;  
    }
}
 
export default Label;