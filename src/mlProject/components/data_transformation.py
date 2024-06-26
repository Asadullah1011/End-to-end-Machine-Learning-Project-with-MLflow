import os
from src.mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config


        ## Note: can add different data transformation techniques such as Scaler, PCA and all
        ## can perform all kind of EDA in ML cycle here before passing the data to the model

        # I am only adding train_test_split cz this data is already cleaned

        

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        #split data into tarain and testing
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index= False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index= False)

        logger.info("Splited data into training and testing")
        logger.info(train.shape)
        logger.info(test.shape)


        print(train.shape)
        print(test.shape)