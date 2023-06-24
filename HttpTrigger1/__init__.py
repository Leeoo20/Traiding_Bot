import logging
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import azure.functions as func

Ibuy = False

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    order = req.params.get('order')
    ticker = req.params.get('ticker')
  
    
    if not order and not ticker :
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:   
            order = req_body.get('order')
            ticker = req_body.get('ticker')
    
    if order == "buy" : 
        if not Ibuy :
            logging.info('Je dois acheter') 
    else : 
        if Ibuy : 
            logging.info('Je dois vendre') 
    

    return func.HttpResponse(f"Bv")
        # return func.HttpResponse(
        #      "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
        #      status_code=200
        # )
