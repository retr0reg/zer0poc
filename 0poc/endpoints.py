import requests
from . import logging

class Target:

    def __init__(
            self,
            url
                 ) -> None:
        
        self.url = url
        self.log = logging.Logger()

        self.log.info(
            f'Created Target: {self.url}\n'
            )
        

    def get_endpoint(
            self,
            url: str,
            action: str
            ):
        
        print('\n')
        self.log.info(f'GET endpoint: {url}')
        self.log.info(f'Action: {action}')
    
        try:
            response = requests.get(url)
        
        except Exception as e:
            self.log.error(f'Error getting endpoint: {e}',
                           indent=2
                           )
            return None
        
        self.log.success(
            f'Endpoint: {url} retrieved successfully',
            indent=2
            )
        
        # log request content
        self.log.info(
            f'Request content: {response.content}',
            indent=2
            )

        return response.content
    
    def post_endpoint(
            self,
            url,
            data,
            action: str
            ):
        
        print('\n')
        self.log.info(f'POST endpoint: {url}')
    
        try:
            response = requests.post(url, data)
        
        except Exception as e:
            self.log.error(f'Error posting endpoint: {e}')
            return None
        
        self.log.success(
            f'Endpoint: {url} posted successfully',
            indent=2
            )
        
        # log request content
        self.log.info(
            f'Request content: {response.content}',
            indent=2
            )

        return response.content
    