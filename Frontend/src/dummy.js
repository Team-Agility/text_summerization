export const dummySteps = {
    "completed": true,
    "status": "Completed",
    "total_steps": 5,
    "completed_steps": 5,
    "all_steps": ["Input", "Feature Extraction" ,"Categorized Sequence", "Word Graph Building", "Path re-ranking", "Output"],
    "steps": [
        {
            "type": "confidenceSequence",
            "step": "Input",
            "data": [
                {
                    "title": "remote control",
                    "acts": [
                        {
                            "act": "Okay", 
                            "confidence":"1",
                        },
                        {
                            "act": "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?",
                            "confidence": "0"
                        }
                    ]
                },
                {
                    "title": "remote control",
                    "acts": [
                        {
                            "act": "Okay", 
                            "confidence":"1",
                        },
                        {
                            "act": "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?",
                            "confidence": "0"
                        }
                    ]
                },
                {
                    "title": "remote control",
                    "acts": [
                        {
                            "act": "Okay", 
                            "confidence":"1",
                        },
                        {
                            "act": "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?",
                            "confidence": "0"
                        }
                    ]
                },
                {
                    "title": "remote control",
                    "acts": [
                        {
                            "act": "Okay", 
                            "confidence":"1",
                        },
                        {
                            "act": "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?",
                            "confidence": "0"
                        }
                    ]
                },
            ]    
        },
        {
            "type": "featureExtraction",
            "step": "Feature Extraction",
            "data": [
                {
                    "title": "remote control",
                    "category" : "Action",
                    "probConfidence": "0",
                    "probUnConfidence": "0",
                    "probNeutral": "0",
                    "noOfSpeakers":5,
                    "noOfUtterances":4,
                    "totalTimeDifference": 3,
                    "overlappingTime":2,
                    "seqLength":451,
                    "acts": ["Okay", "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?"]
                },
                {
                    "title": "xyz",
                    "category" : "Decision",
                    "probConfidence": "0",
                    "probUnConfidence": "0",
                    "probNeutral": "0",
                    "noOfSpeakers":5,
                    "noOfUtterances":4,
                    "totalTimeDifference": 3,
                    "overlappingTime":2,
                    "seqLength":451,
                    "acts": ["Okay", "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?"]
                },
                {
                    "title": "xyz",
                    "category" : "Problem",
                    "probConfidence": "0",
                    "probUnConfidence": "0",
                    "probNeutral": "0",
                    "noOfSpeakers":5,
                    "noOfUtterances":4,
                    "totalTimeDifference": 3,
                    "overlappingTime":2,
                    "seqLength":451,
                    "acts": ["Okay", "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?"]
                },
                {
                    "title": "xyz",
                    "category" : "Abstract",
                    "probConfidence": "0",
                    "probUnConfidence": "0",
                    "probNeutral": "0",
                    "noOfSpeakers":5,
                    "noOfUtterances":4,
                    "totalTimeDifference": 3,
                    "overlappingTime":2,
                    "seqLength":451,
                    "acts": ["Okay", "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?"]
                }
            ]    
        },
        {
            "type": "categorizedSequence",
            "step": "Categorized Sequence",
            "data": [
                {
                    "title": "remote control",
                    "category" : "Action",
                    "acts": ["Okay", "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?"]
                },
                {
                    "title": "xyz",
                    "category" : "Decision",
                    "acts": ["Okay", "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?"]
                },
                {
                    "title": "xyz",
                    "category" : "Problem",
                    "acts": ["Okay", "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?"]
                },
                {
                    "title": "xyz",
                    "category" : "Abstract",
                    "acts": ["Okay", "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?"]
                }
            ]    
        },
        {
            "type": "imageArray",
            "step": "Word Graph Generate",
            "data": [
                "https://concisesoftware.com/wp-content/uploads/2019/05/Concise-Software-Scrum-meeting.jpg",
                "https://concisesoftware.com/wp-content/uploads/2019/05/Concise-Software-Scrum-meeting.jpg",
                "https://concisesoftware.com/wp-content/uploads/2019/05/Concise-Software-Scrum-meeting.jpg",
                "https://concisesoftware.com/wp-content/uploads/2019/05/Concise-Software-Scrum-meeting.jpg"
            ]
        },
        {
            "type": "summery",
            "step": "Path re-ranking",
            "data": [
                {
                    "wordGraph":"https://concisesoftware.com/wp-content/uploads/2019/05/Concise-Software-Scrum-meeting.jpg",
                    "acts": ["Okay", "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?"],
                    "category" : "Action",
                    "summery" :"This is the summery sentences"
                },
                {
                    "wordGraph":"https://concisesoftware.com/wp-content/uploads/2019/05/Concise-Software-Scrum-meeting.jpg",
                    "acts": ["Okay", "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?"],
                    "category" : "Action",
                    "summery" :"This is the summery sentences"
                },
                {
                    "wordGraph":"https://concisesoftware.com/wp-content/uploads/2019/05/Concise-Software-Scrum-meeting.jpg",
                    "acts": ["Okay", "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?"],
                    "category" : "Action",
                    "summery" :"This is the summery sentences"
                },
                {
                    "wordGraph":"https://concisesoftware.com/wp-content/uploads/2019/05/Concise-Software-Scrum-meeting.jpg",
                    "acts": ["Okay", "Um well this is the kick-off meeting for our our project. Um and um this is just what we're gonna be doing over the next twenty five minutes. Um so first of all, just to kind of make sure that we all know each other, I'm Laura and I'm the project manager. Do you want to introduce yourself again?"],
                    "category" : "Action",
                    "summery" :"This is the summery sentences"
                }
            ]
        },
        {
            "type": "abstractiveSummery",
            "step": "Output",
            "data": [
                {
                    "category": "Abstract",
                    "summery": ["The project manager introduced the upcoming project to the team members and then the team members participated in an exercise in which they drew their favorite animal and discussed what they liked about the animal.",
                    "The project manager talked about the project finances and selling prices.",
                    "The team then discussed various features to consider in making the remote."]
                },
                {
                    "category": "Decision",
                    "summery": [  "The industrial designer will work on the working design of the remote.",
                    "The user interface designer will work on the technical functions of the remote.",
                    "The marketing executive will work on what requirements the remote has to fulfill"]
                },
                {
                    "category": "Action",
                    "summery": [  "The remote will sell for 25 Euro.",
                    "The remote will be sold on an international scale.",
                    "The production costs cannot exceed 12.50 Euro."]
                },
                {
                    "category": "Problem",
                    "summery": ["Whether the remote will be used exclusively for televisions."]
                }
            ]    
        }
    ]
  }
