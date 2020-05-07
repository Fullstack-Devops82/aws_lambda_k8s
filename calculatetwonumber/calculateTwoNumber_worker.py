import logging
import json
from stefuna import Worker


logger = logging.getLogger('stefuna.info')
logger.setLevel(logging.INFO)
stream_hander = logging.StreamHandler()
logger.addHandler(stream_hander)

class CalculateTwoNumberWorker(Worker):
    def init(self):
        """Initialize the single instance in a worker"""
        # self.config is the worker config
        logger.info('Init CalculateTwoNumber worker instance')

    def run_task(self, task_token, input_data):
        logger.info('CalculateTwoNumber Worker in run_task')

        # numberOne = input_data['numberOne']

        return {"message": "CalculateTwoNumber Worker success, launch DisplayFirstMessage Worker."}
