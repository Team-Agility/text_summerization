import React from "react";
import { Card } from "antd";

function ConfidenceFile({ data }) {
  console.log("ConfidenceFile - data : ", data);
  return (
    <Card>
      confidence : <a href={data.confidence}>Confidence json file</a>
      <br />
      sequences : <a href={data.sequences}>Sequences json file</a> <br />
      transcript : <a href={data.transcript}>Transcript json file</a> <br />
    </Card>
  );
}

export default ConfidenceFile;
