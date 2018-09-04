#Q.1-Use the "https://api.forismatic.com/api/1.0/" api to get random quotes using the correct endpoints.

import requests
info=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
print(info.status_code)
import json
detail=info.json()
print(type(detail))
print(detail["quoteText"])
