"""Module for handling autocomplete's part of the API"""

from domain.constants import API_BASE
from domain.general import send_post, get, validate_params

BASE = API_BASE + "autocomplete"

def autocomplete(query, **kwargs):
    target = BASE 
    
    options = []
    options.append('?query=' + query)
    for item in kwargs.items():
        options.append(item[0] + '=' +  str(item[1]))
    #TODO: specify product=hotels as default, else this does strange things
    target += '&'.join(options)
    response = get(target)
    return response