# Fake news detector
Live view\
[http://serve-sentiment-env.eba-dqpfwvjj.us-east-2.elasticbeanstalk.com/](http://serve-sentiment-env.eba-dqpfwvjj.us-east-2.elasticbeanstalk.com/)

## API
prediction endpoint is `/predict`\
POST input json with `{'text': 'your news article'}`\
The model will return `{'prediction': 'REAL'}` or `{'prediction': 'FAKE'}`

# Performance Stress Test
![Can be found here](./ec2_stresstest/execution_times.png)
