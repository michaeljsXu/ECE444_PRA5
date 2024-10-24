# Fake news detector
Live view: [http://serve-sentiment-env.eba-dqpfwvjj.us-east-2.elasticbeanstalk.com/](http://serve-sentiment-env.eba-dqpfwvjj.us-east-2.elasticbeanstalk.com/)
![image](https://github.com/user-attachments/assets/eff8be13-83e8-4cf1-aa95-2b7c38121052)

## API
prediction endpoint is `/predict`\
POST input json with `{'text': 'your news article'}`\
The model will return `{'prediction': 'REAL'}` or `{'prediction': 'FAKE'}`

# Performance Stress Test
![Can be found here](./ec2_stresstest/execution_times.png)
