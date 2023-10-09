import requests
import os

from django.conf import settings

rakuten_ichiba_item_search_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601?'

HITS_PER_PAGE = 10

def get_products_by_product_ids(cart_items):
    product_info_list = []

    for cart_item in cart_items:
        params = {
            'applicationId': settings.APPLICATION_ID,
            'itemCode': cart_item.product_id,
            'formatVersion': 2,
        }
        response = requests.get(rakuten_ichiba_item_search_url, params=params)

        if response.status_code == 200:
            data = response.json()
            product_info = data['Items'][0]
            product_info['cart_id'] = cart_item.id
            product_info_list.append(product_info)

    return product_info_list

#def get_products_list(shop_code):
#    req_params['shopCode'] = shop_code
#    res = requests.get(REQ_URL, params=req_params)
#    #pprint.pprint(res)
#    res_json = res.json()['Items']
#    """
#    for product in res_json['Items']:
#        products_list.append({
#            'product_id':product['Item']['itemCode'],
#            'product_name':product['Item']['itemName'],
#            'product_price':product['Item']['itemPrice'],
#            'product_url':product['Item']['itemUrl'],
#            'product_image_url':product['Item']['mediumImageUrls'][0]['imageUrl'],
#        })
#    """
#    return res_json

def get_products_by_shop_code(shop_code):
    params = {
        'applicationId': settings.APPLICATION_ID,
        'shopCode': shop_code,
        'formatVersion': 2,
        'hits': HITS_PER_PAGE,
    }
    response = requests.get(rakuten_ichiba_item_search_url, params=params)

    if response.status_code == 200:
        data = response.json()['Items']
        return data

    return []

def get_products_by_item_code(item_code):
    params = {
        'applicationId': settings.APPLICATION_ID,
        'itemCode': item_code,
        'formatVersion': 2,
        'hits': HITS_PER_PAGE,
    }
    response = requests.get(rakuten_ichiba_item_search_url, params=params)

    if response.status_code == 200:
        data = response.json()['Items']
        return data

    return []

