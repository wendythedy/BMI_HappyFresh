import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def main(event, context):
    logger.info('**********Request**********')
    logger.info(event)

    height = event['height']
    weight = event['weight']
    bmi = round(weight/(height/100)**2,2)

    if(bmi>=18.5) and (bmi<=24.9):
        response = {
            "statusCode": 200,
            "bmi": bmi,
            "label":"healthy",
            "message": "success"
        }
    elif(bmi>=25):
        response = {
            "statusCode": 200,
            "bmi": bmi,
            "label":"overweight",
            "message": "success"
        }
    else:
        response = {
            "statusCode": 200,
            "bmi": bmi,
            "label":"unclassified",
            "message": "error input"
        }
    logger.info('**********Response**********')
    logger.info(response)    
    return response