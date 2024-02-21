
import re
from core.requester import requester

# def check_response(request,params):

#     response = requester(request)
#     if type(response) != str and response.status_code in (400, 413, 418, 429, 503):
#         return []
#     if type(response) ==str:
#         return []

#     value='"dalaho'
#     if value in response.text and re.search(r'[\'"\s]%s[\'"\s]' % value, response.text):
#         reftected_params=[]
#         for val in params.values():
#             if val in response.text and re.search(r'[\'"\s]%s[\'"\s]' % val, response.text):
#                 reftected_params.append(val)
#         return reftected_params

    
# def bruter(request, params):
#     """
#     returns anomaly detection result for a chunk of parameters
#     returns list
#     """

#     response = requester(request, params)

#     reftected_params = check_response(response, params)
#     if reftected_params:
#         return reftected_params
#     else:
#         return []
      
def bruter(request, params):
  
    response = requester(request, params)

    if type(response) != str and response.status_code in (400, 413, 418, 429, 503):
        return False
    if type(response) ==str:
        return False
    
    value='"dalaho'
    if value in response.text and re.search(r'[\'"\s]%s[\'"\s]' % value, response.text):
        return True
    else:
        return False
