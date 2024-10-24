# Fake news detector
Live view: [http://serve-sentiment-env.eba-dqpfwvjj.us-east-2.elasticbeanstalk.com/](http://serve-sentiment-env.eba-dqpfwvjj.us-east-2.elasticbeanstalk.com/)
![sample](https://github.com/user-attachments/assets/d9a1fe72-2006-4965-9209-68884b3fd05e)


## API
prediction endpoint is `/predict`\
POST input json with `{'text': 'your news article'}`\
The model will return `{'prediction': 'REAL'}` or `{'prediction': 'FAKE'}`

# Performance Stress Test
![Can be found here](./ec2_stresstest/execution_times.png)
