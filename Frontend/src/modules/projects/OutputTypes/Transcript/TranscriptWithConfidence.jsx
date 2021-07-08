import React from 'react'
import { Card } from 'antd';

export default function TranscriptWithConfidence({data}) {
    const { acts } =data
    console.log("TranscriptWithConfidence : ", data)
    return (
        <React.Fragment>
            <Card title={`TranscriptWithConfidence`}>
                {data && data.map((act,i)=>{
                    return(
                        <div key={i}>
                            <p>Act :  {act["act"]}</p>
                            <p>Confidence :  {act["confidence"]}</p>
                            <p>Speaker ID :  {act["speaker_id"]}</p>
                            <p>Start time :  {act["start_time"]}</p>
                            <p>End time :  {act["end_time"]}</p>
                            <hr/>
                        </div>
                    )
                })}
            </Card>
        </React.Fragment>
       
    )
}
