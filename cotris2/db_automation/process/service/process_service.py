from abc import ABC, abstractmethod
from db_automation.process.service.process_service_impl import ProcessServiceImpl


class ProcessService(ProcessServiceImpl):

    @abstractmethod
    def process_fruit(self):
        pass