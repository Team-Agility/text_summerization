import React from "react";
import { Card } from "antd";

function SequenceTaggingFeatureExtraction({ data }) {
  console.log("SequenceTaggingFeatureExtraction - data : ", data);
  return (
    <div>
      {data &&
        data.map((seq, i) => {
          return (
            <Card id={i}>
              <h3>Category : {seq.category} </h3>
              No of speakers : {seq.no_of_speakers} <br />
              No of utterances : {seq.no_of_utterances} <br />
              Overlapping Time : {seq.overlapping_time} <br />
              Probability of confidence utterance :{" "}
              {seq.prob_of_confidence_utterances} <br />
              Probability of neutral utterance :{" "}
              {seq.prob_of_neutral_utterances} <br />
              Probability of un-confidence utterance :{" "}
              {seq.prob_of_unconfident_utterances} <br />
              Total no of time difference : {
                seq.total_no_of_time_difference
              }{" "}
              <br />
              Total no of utterance length : {
                seq.total_no_of_utterance_length
              }{" "}
              <br />
              Total sequence duration : {seq.total_sequence_duration} <br />
            </Card>
          );
        })}
    </div>
  );
}

export default SequenceTaggingFeatureExtraction;
