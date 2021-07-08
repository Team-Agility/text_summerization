import React from 'react'
import { Card } from 'antd';
import ImageHolder from "../Image/ImageHolder"
import Acts from '../Sequence/Acts';

function ConfidenceSequence({data}) {
    console.log("ConfidenceSequence - data : ", data)
    return (
        <div>
            {
                data && data.map((act,i)=>{
                    return(
                        <div key={act.id}>
                            <p>ID : {act.id}</p>
                            <p>Act : {act.act}</p>
                            <p>Confident : {act.confidence}</p>
                            <p>End Time : {act.end_time}</p>
                            <hr />
                        </div>
                    )
                })
            }
        </div>
    )
}

export default ConfidenceSequence
