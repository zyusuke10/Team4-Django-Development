import requests
import os

rakuten_ichiba_item_search_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601?'
rakuten_application_id = os.environ.get('APPLICATION_ID')

def get_products_by_product_ids(cart_items):
    product_info_list = []

    for cart_item in cart_items:
        params = {
            'applicationId': rakuten_application_id,
            'itemCode': cart_item.product_id,
            'formatVersion': 2,
        }
        response = requests.get(rakuten_ichiba_item_search_url, params=params)

        if response.status_code == 200:
            data = response.json()
            product_info = data['Items'][0]
            product_info['cart_id'] = cart_item.id
            print(product_info)
            product_info_list.append(product_info)

    return product_info_list

def get_products_by_shop_code(shop_code):
    params = {
        'applicationId': rakuten_application_id,
        'shopCode': shop_code,
    }
    response = requests.get(rakuten_ichiba_item_search_url, params=params)

    if response == 200:
        data = response.json()
        return data

    return []

