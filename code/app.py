import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def main(event, context):
    logger.info('********************Request********************')
    logger.info(event)

    #Validate
    if (event['height'].isnumeric() == False) or (event['weight'].isnumeric() == False):
        response = {
            "statusCode": 200,
            "bmi": "-",
            "label":"-",
            "message": "the height or weight cannot be string"
        }
        logger.info('********************Response********************')
        logger.info(response)    
        return response
    elif (int(event['height']) <= 0) or (int(event['weight']) <= 0):
        response = {
            "statusCode": 200,
            "bmi": "-",
            "label":"-",
            "message": "the height or weight cannot be negative or zero"
        }
        logger.info('********************Response********************')
        logger.info(response)    
        return response
        
        
    #Logic
    height = int(event['height'])
    weight = int(event['weight'])
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
            "message": "success"
        }
    logger.info('********************Response********************')
    logger.info(response)    
    return response