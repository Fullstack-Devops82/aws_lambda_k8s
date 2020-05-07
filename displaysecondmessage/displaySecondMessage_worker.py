import logging
from stefuna import Worker

logger = logging.getLogger('stefuna.log')

class DisplaySecondMessageWorker(Worker):

    def init(self):
        """Initialize the single instance in a worker"""
        # self.config is the worker config
        self.logger.debug('Init DisplaySecondMessage worker instance')


    def run_task(self, task_token, input_data):
        self.logger.debug('DisplaySecondMessage Worker in run_task')
        # numberFirst = input_data['numbertwo']


        return {"message": "DisplaySecondMessage Worker End"}
