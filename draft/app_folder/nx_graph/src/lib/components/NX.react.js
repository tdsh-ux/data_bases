import React, {Component} from 'react';
import PropTypes from 'prop-types';
import nxWidget from "../render/nx_render.js";

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class NX extends Component {

    componentDidMount() {
        const {id, setProps, data} = this.props;
        // const self = this;
        this.nx = new nxWidget(this.el, data, figure => {
            console.log(figure);
            setProps({tapNode: figure});
        });

    }

    componentDidUpdate() {

      const {id, setProps, data} = this.props;
      if(data == this.nx.data) {return;}
      // this.nx.setCanvas();
      // console.log(data);
      setTimeout(() => {this.nx.drawGraph(data)}, 148);
    }

    render() {

        const {id, setProps, data} = this.props;
        return (
            <div id={id} ref = {el => this.el = el}></div>
        );
    }
}

NX.defaultProps = {};

NX.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

    /**
    * Vega-lite specification of the plot.
    */
    data: PropTypes.object.isRequired,

    /**
    * Node clicked.
    */
    tapNode: PropTypes.object,
};
