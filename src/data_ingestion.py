import os
import numpy as np 
import pandas as pd 
from google.cloud import storage
from config.paths_config import *
from utils.common_function import read_yaml
from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self , config):
        self.config = config['data_ingestion']
        self.raw_dir = RAW_DIR
        self.bucket_name = self.config['bucket_name']
        self.source_file_name = self.config['source_file_name']
         
        os.makedirs(self.raw_dir, exist_ok=True)
        logger.info("DataIngestion initialized")

    def download_files(self):
        try:
            client = storage.Client()
            bucket = client.get_bucket(self.bucket_name)
            for file_name in self.source_file_name:
                logger.info(f"Downloading file {file_name}")
                file_path = os.path.join(self.raw_dir, file_name)
                if file_name == "animelist.csv":
                    
                    blob = bucket.blob(file_name)
                    blob.download_to_filename(os.path.join(self.raw_dir, file_name))
                    data = pd.read_csv(file_path)
                    data.to_csv(file_path, index=False)
                    logger.info(f"File {file_name} downloaded successfully")
                else:
                    blob = bucket.blob(file_name)
                    blob.download_to_filename(os.path.join(self.raw_dir, file_name))
                    logger.info(f"File {file_name} downloaded successfully")
        except Exception as e:
            logger.error(f"Error while downloading files: {e}")
            raise CustomException(e, sys)
    

    def run(self):
        try:
            logger.info("DataIngestion run method started")
            self.download_files()
            logger.info("DataIngestion run method completed")
        except Exception as e:
            logger.error(f"Error while running DataIngestion: {e}")
            raise CustomException(e, sys)

    
if __name__ == "__main__":
    config = read_yaml(CONFIR_DIR)
    data_ingestion = DataIngestion(config)
    data_ingestion.run()
    