from src.mowingEstimator.logging import logger
from src.mowingEstimator.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.mowingEstimator.pipeline.stage_2_data_validation_pipeline import DataValidationTrainingPipeline
from src.mowingEstimator.pipeline.stage_3_data_transformation_pipeline import DataTransformationTrainingPipeline
from src.mowingEstimator.pipeline.stage_4_model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.mowingEstimator.pipeline.stage_5_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation_pipeline = DataValidationTrainingPipeline()
   data_validation_pipeline.initiate_data_validation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation_pipeline = DataTransformationTrainingPipeline()
   data_transformation_pipeline.initiate_data_transformation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_trainer_pipeline = ModelTrainerTrainingPipeline()
   data_trainer_pipeline.initiate_model_training()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_evaluation_pipeline = ModelEvaluationTrainingPipeline()
   data_evaluation_pipeline.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
