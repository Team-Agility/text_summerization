import React from 'react'
import { Card } from 'antd';

export default function Transcript({data}) {
    const { acts } =data
    console.log("Transcript : ", data)
    return (
        <React.Fragment>
            <Card title={`Transcript`}>
                {acts && acts.map((content,i)=>{
                    return(
                        <div key={i}>
                            <p>content :  {content["segment"]}</p>
                            <p>end_time :  {content["end_time"]}</p>
                            <p>is_punction :  {content["is_punction"]? "True" : "False"}</p>
                            <p>speaker_id :  {content["speaker_id"]}</p>
                            <p>start_time :  {content["start_time"]}</p>
                            <hr/>
                        </div>
                    )
                })}
            </Card>
        </React.Fragment>
       
    )
}
