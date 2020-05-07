This is an example to trigger Web API on Kubernetes using AWS Lambda and Step Function.

Here are some commands to build the environment.
```sh
$ pip install boto3
$ pip install stefuna
$ pip install awscli


$ npm install -g serverless
$ npm install -g serverless serverless-step-functions
$ serverless plugin install --name serverless-step-functions
$ npm install --save-dev serverless-pseudo-parameters
$ serverless plugin install --name serverless-pseudo-parameters
$ serverless config credentials --provider aws --key [KEY] --secret [SECRET]

$ stefuna --config=calculateTwoNumber_config
$ stefuna --config=displayFirstMessage_config
$ stefuna --config=displaySecondMessage_config


- deploy
$ serverless deploy
```