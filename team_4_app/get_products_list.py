from django.conf import settings
import requests,json,datetime,os,re
import pprint

REQ_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601'
HITS_PER_PAGE = 10

req_params = {
    'applicationId':os.environ.get('APPLICATION_ID'),
    'format':'json',
    'formatVersion':'2',
    'shopCode':'',
    'hits': HITS_PER_PAGE,
}

def get_products_list(shop_code):
    req_params['shopCode'] = shop_code
    res = requests.get(REQ_URL, params=req_params)
    #pprint.pprint(res)
    res_json = res.json()['Items']
    """
    for product in res_json['Items']:
        products_list.append({
            'product_id':product['Item']['itemCode'],
            'product_name':product['Item']['itemName'],
            'product_price':product['Item']['itemPrice'],
            'product_url':product['Item']['itemUrl'],
            'product_image_url':product['Item']['mediumImageUrls'][0]['imageUrl'],
        })
    """
    return res_json
