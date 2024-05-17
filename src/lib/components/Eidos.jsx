import React, { useCallback, useEffect, useState, useRef } from "react";

import "./style.css";

const Eidos = ({
  id,
  eidos,
  spectype,
  width = "100%",
  height = 500,
  events = [],
  renderer = "https://render.eidos.oceanum.io",
  setProps,
}) => {
  const [init, setInit] = useState(false);
  const container = useRef(null);
  const iframeRef = useRef(null);

  useEffect(() => {
    if (iframeRef.current) {
      window.addEventListener("message", handleMessage);
    }
  }, []);

  useEffect(() => {
    updateSpec(eidos, spectype);
  }, [eidos, spectype]);

  const handleMessage = useCallback(
    (message) => {
      const { data } = message;
      if (data.action === "status" && data.data.status === "ready") {
        updateSpec(eidos, spectype);
        setInit(true);
      } else if (events.includes(data.action)) {
        setProps({
          lastevent: data,
        });
      }
    },
    [events]
  );

  const updateSpec = useCallback(
    (spec, spectype) => {
      const messageTarget = iframeRef.current.contentWindow;
      messageTarget.postMessage({ id, type: spectype, payload: spec }, "*");
    },
    [iframeRef]
  );

  return (
    <div
      className="eidos-component"
      style={{ height, width, position: "relative" }}
      ref={container}
    >
      <iframe
        title="Eidos"
        src={`${renderer}?id=${id}`}
        style={{ width: "100%", height: "100%", border: "none" }}
        ref={iframeRef}
      ></iframe>
    </div>
  );
};

export default Eidos;
