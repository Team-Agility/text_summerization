import React from "react";
import { Card } from "antd";

export default function SummaryCategorizedSequence({ data }) {
  console.log("SummaryCategorizedSequence : data : ", data);
  const { actions, decisions, problems } = data;
  return (
    <React.Fragment>
      <Card>
        <h3>Actions</h3>
        {actions.map((act, i) => {
          return (
            <div key={act[0].id}>
              <p>ID : {act[0].id}</p>
              <p>Act : {act[0].act}</p>
              <p>Confident : {act[0].confidence}</p>
              <p>End Time : {act[0].end_time}</p>
              <p>word_range : {act[0].word_range}</p>
              <hr />
            </div>
          );
        })}
      </Card>

      <Card>
        <h3>Decisions</h3>
        {decisions.map((act, i) => {
          return (
            <div key={act[0].id}>
              <p>ID : {act[0].id}</p>
              <p>Act : {act[0].act}</p>
              <p>Confident : {act[0].confidence}</p>
              <p>End Time : {act[0].end_time}</p>
              <p>word_range : {act[0].word_range}</p>
              <hr />
            </div>
          );
        })}
      </Card>

      <Card>
        <h3>Problems</h3>
        {problems.map((act, i) => {
          return (
            <div key={act[0].id}>
              <p>ID : {act[0].id}</p>
              <p>Act : {act[0].act}</p>
              <p>Confident : {act[0].confidence}</p>
              <p>End Time : {act[0].end_time}</p>
              <p>word_range : {act[0].word_range}</p>
              <hr />
            </div>
          );
        })}
      </Card>
    </React.Fragment>
  );
}
