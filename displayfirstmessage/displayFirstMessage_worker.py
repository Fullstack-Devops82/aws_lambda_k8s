import logging
import json
# from displaySecondMessage_worker import DisplaySecondMessageWorker
from stefuna import Worker

logger = logging.getLogger('stefuna.log')
logger.setLevel(logging.INFO)
stream_hander = logging.StreamHandler()
logger.addHandler(stream_hander)

class DisplayFirstMessageWorker(Worker):

    def init(self):
        """Initialize the single instance in a worker"""
        # self.config is the worker config
        logger.debug('Init DisplayFirstMessage worker instance')


    def run_task(self, task_token, input_data):
        logger.debug('DisplayFirstMessage Worker in run_task')
        # numberFirst = input_data['numberone']

        return {"message": "DisplayFirstMessage Worker success, launch DisplaySecondMessage Worker."}
