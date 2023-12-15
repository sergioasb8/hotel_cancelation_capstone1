import requests

data = {
    'lead_time':39,
    'arrival_year':2019,
    'avg_price_per_room':102.12,
    'no_of_special_requests':2,
    'market_segment_type':1,
}

local_url = 'http://0.0.0.0:9696/hotel_cancelation'

resp = requests.post(local_url, json=data).json()

print(resp)