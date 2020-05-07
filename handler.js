'use strict';

const AWS = require('aws-sdk');
const stepfunctions = new AWS.StepFunctions();

module.exports.executeStepFunction = (event, context, callback) => {
  console.log('executeStepFunction');

  const numberOne = event.queryStringParameters.numberOne;
  const numberTwo = event.queryStringParameters.numberTwo;
  console.log(numberOne);
  console.log(numberTwo);

  callStepFunction(numberOne, numberTwo).then(result => {
    let message = 'Step function is executing';
    if (!result) {
      message = 'Step function is not executing';
    }

    const response = {
      statusCode: 200,
      body: JSON.stringify({ message })
    };

    callback(null, response);
  });
};


function callStepFunction(numberOne, numberTwo) {
  console.log('callStepFunction');

  const stateMachineName = 'SequenceActivityMachine'; // The name of the step function we defined in the serverless.yml
  console.log('Fetching the list of available workflows');

  return stepfunctions
    .listStateMachines({})
    .promise()
    .then(listStateMachines => {
      console.log('Searching for the step function', listStateMachines);

      for (var i = 0; i < listStateMachines.stateMachines.length; i++) {
        const item = listStateMachines.stateMachines[i];

        if (item.name.indexOf(stateMachineName) >= 0) {
          console.log('Found the step function', item);

          var params = {
            stateMachineArn: item.stateMachineArn,
            input: JSON.stringify({ numberOne: numberOne, numberTwo: numberTwo })
          };

          console.log('Start execution');
          return stepfunctions.startExecution(params).promise().then(() => {
            return true;
          });
        }
      }
    })
    .catch(error => {
      return false;
    });
}
