import logging


#logging.basicConfig(filename='test_log.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

class LogFunc:
    def get_log(self):
        # Create a logger
        logger = logging.getLogger('report_log')
        logger.setLevel(logging.DEBUG)

        # Create a file handler with formatter
        log_path = 'C:\\Users\\Angelica\\PycharmProjects\\AutomationExercises\\Logs\\log_report.log'
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(formatter)

        # Remove any existing handlers to fix duplicate logs
        logger.handlers.clear()

        # Add the file handler to the logger
        logger.addHandler(file_handler)

        return logger





