import React, { useEffect, useRef } from "react";
import PropTypes from "prop-types";

import Eidos from "./Eidos.jsx";

/**
  DashEidos is a an EIDOS visualisation component for Dash.
  It takes a EIDOS spec, converts it to a React component in a Plotly dash app,
 */

const DashEidos = (props) => {
  return (
    <React.Suspense fallback={<div>Loading map...</div>}>
      <Eidos {...props} />
    </React.Suspense>
  );
};

DashEidos.defaultProps = {
  spectype: "spec",
  width: "100%",
  height: 500,
  events: ["click"],
  renderer: "https://render.eidos.oceanum.io",
};

DashEidos.propTypes = {
  /**
   * The ID used to identify this component in Dash callbacks.
   */
  id: PropTypes.string.isRequired,

  /**
   * Eidos spec
   */
  eidos: PropTypes.object.isRequired,

  /**
   * The type of spec. Can be either 'spec' or 'patch'.
   *
   */
  spectype: PropTypes.oneOf(["spec", "patch"]),

  /**
   * An array of tooltip objects that follows he pydeck tooltip specifcation.
   * An additonal 'layer' property can be added to the tooltip objects to restrict their action to that layer ID.
   */
  width: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),

  /**
   * Height of the map component container as pixels or CSS string
   * (optional) Default 500
   */
  height: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),

  /**
   * List of EIDOS events to listen to. Can be any of:
   * ['click']
   */
  events: PropTypes.array,

  /**
   * The last event that was triggered. This is a read-only property.
   */
  lastevent: PropTypes.object,

  /**
   * The URL of the EIDOS renderer.
   */
  renderer: PropTypes.string,
};

export const defaultProps = DashEidos.defaultProps;
export const propTypes = DashEidos.propTypes;
export default DashEidos;
