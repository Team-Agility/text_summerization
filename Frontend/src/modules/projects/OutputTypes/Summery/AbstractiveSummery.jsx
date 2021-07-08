import React from "react";
import { Card } from "antd";
import { CaretRightOutlined } from "@ant-design/icons";

function AbstractiveSummery({ data }) {
  console.log("AbstractiveSummery ~ data", data);
  const { actions, decisions, problems } = data;

  return (
    <Card title="Meeting Summery">
      <React.Fragment>
        <h3>Actions</h3>
        {actions.map((item, i) => {
          return (
            <React.Fragment>
              <div key={i}>
                <CaretRightOutlined />
                {item}
              </div>
              <br />
            </React.Fragment>
          );
        })}
      </React.Fragment>

      <React.Fragment>
        <h3>Decisions</h3>
        {decisions.map((item, i) => {
          return (
            <React.Fragment>
              <div key={i}>
                {" "}
                <CaretRightOutlined />
                {item}
              </div>
              <br />
            </React.Fragment>
          );
        })}
      </React.Fragment>

      <React.Fragment>
        <h3>Problems</h3>
        {problems.map((item, i) => {
          return (
            <React.Fragment>
              <div key={i}>
                {" "}
                <CaretRightOutlined />
                {item}
              </div>
              <br />
            </React.Fragment>
          );
        })}
      </React.Fragment>
    </Card>
  );
}

export default AbstractiveSummery;
