
import requests
import warnings

import core.config as mem



warnings.filterwarnings('ignore') # Disable SSL related warnings

def requester(request, payload={}):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1'
    }

    
    session=requests.Session()
    try:
        response =  session.get(request,
            params=payload,
            verify=False,
            headers=headers,
            allow_redirects=False
        )
    
        return response
    except Exception as e:
        return str(e)

