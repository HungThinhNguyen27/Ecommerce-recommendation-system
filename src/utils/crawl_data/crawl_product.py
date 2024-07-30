from tqdm import tqdm
import random
import time
import requests
import pandas as pd
import json


with open('crawl_data/request_metadata.json', 'r') as file:
    data = json.load(file)

cookies = data.get('cookies', {})
headers = data.get('headers', {})
params = data.get('params', {})


def parser_product(json):
    d = dict()
    d['id'] = json.get('id')
    d['short_description'] = json.get('short_description')
    d['price_sale'] = json.get('price')
    d['price_source'] = json.get('list_price')
    d['discount'] = json.get('discount')
    d['discount_rate'] = json.get('discount_rate')
    d['review_count'] = json.get('review_count')
    d['order_count'] = json.get('order_count')
    d['stock_item_qty'] = json.get('stock_item').get('qty')
    d['product_name'] = json.get('meta_title')
    d['brand_id'] = json.get('brand').get('id')
    d['brand_name'] = json.get('brand').get('name')
    print(d)
    return d


df_id = pd.read_csv('crawl_data/product_id_ncds.csv')
p_ids = df_id.id.to_list()
print(p_ids)
result = []
for pid in tqdm(p_ids, total=len(p_ids)):
    response = requests.get('https://tiki.vn/api/v2/products/{}'.format(pid),
                            headers=headers,
                            params=params,
                            cookies=cookies)

    if response.status_code == 200:
        print('Crawl data {} success !!!'.format(pid))
        result.append(parser_product(response.json()))
    time.sleep(random.randrange(1, 2))
# Save to JSON file
with open('crawled_data_ncds.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
