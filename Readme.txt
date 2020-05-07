This is an example to trigger Web API on Kubernetes using AWS Lambda and Step Function.

Here are some commands to build the environment.

$ pip install boto3
$ pip install stefuna
$ pip install awscli


$ npm install -g serverless
$ npm install -g serverless serverless-step-functions
$ serverless plugin install --name serverless-step-functions
$ npm install --save-dev serverless-pseudo-parameters
$ serverless plugin install --name serverless-pseudo-parameters
$ serverless config credentials --provider aws --key AKIA5JBOUSTDLIYYQT6Q --secret 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

$ stefuna --config=calculateTwoNumber_config
$ stefuna --config=displayFirstMessage_config
$ stefuna --config=displaySecondMessage_config


- deploy
$ serverless deploy

- Catch log
$ serverless logs -f executeStepFunction -t


- Build docker image
$ sudo docker build -t calculatetwonumber --build-arg AWS_ACCESS_KEY="AKIA5JBOUSTDLIYYQT6Q" --build-arg AWS_SECRET_ACCESS_KEY="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" .
$ sudo docker tag dreamy_aryabhata nazarm1994/calculatetwonumber:1
$ sudo docker run -it calculatetwonumber



- kubernetes commands
. List all containers in a Pod
$ kubectl get pods [pod-name-here] -n [namespace] -o jsonpath='{.spec.containers[*].name}'

. Connect to container in Pod
$ kubectl exec -it [Pod Name] -- /bin/bash
$ kubectl exec -it [Pod Name] --container [Container Name] -- /bin/bash

. Check the logs of Pod
$ kubectl logs -f [Pod Name]
$ kubectl logs -f [Pod Name] [Container Name]
$ kubectl logs --previous [Pod Name] [Container Name]
$ kubectl --v=8 logs [Pod Name]

. Describe Pod
$ kubectl describe pod [Pod Name]

. Delete Pod
$ kubectl get deployments --all-namespaces
$ kubectl delete deployment [Name]

. Create Deployment
$ kubectl create deployment [Name] --image=[Docker Hub Path]

. Run Pod
$ kubectl run displayfirstmessage -it --image=nazarm1994/displayfirstmessage:2

. Get services
$ kubectl get services

. Public Pods
$ kubectl expose deployment [Name] --type=LoadBalancer --port=8080
