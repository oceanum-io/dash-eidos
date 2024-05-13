import React, { useState, useCallback } from "react";
import DashEidos from "../lib/components/DashEidos.react";
import spec from "./spec.json";

const App = () => {
  const [state, setState] = useState({
    id: "eidos_test",
    eidos: spec,
    spectype: "spec",
    height: 800,
    events: ["click"],
    lastevent: null,
    renderer: "http://localhost:3001",
  });

  const setProps = (newProps) => {
    setState((prevState) => ({
      ...prevState,
      ...newProps,
    }));
  };

  return (
    <div>
      <DashEidos setProps={setProps} {...state} />
      <div>{state.lastevent && JSON.stringify(state.lastevent.coordinate)}</div>
    </div>
  );
};

export default App;
