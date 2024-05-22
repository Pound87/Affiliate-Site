import requests
import re, iop

appkey = 503784
appSecret = "cDKOdtBHzsQgC8bex7t0bw58zXhbWX89"


def get_item_id_from_url(product_url):
    pattern = r'/(\d+).html'
    match = re.search(pattern, product_url)
    if match:
        item_id = match.group(1)
        return item_id
    else:
        return None

def get_details_by_item_id(itmurl):
    try:
        item_id = get_item_id_from_url(itmurl)
        if item_id:
            req = requests.get(f'https://www.aliexpress.com/item/{item_id}.html')
            image = re.search('<meta property="og:image" content="(.*?)"/>', req.text) if req else None
            client = iop.IopClient('https://api-sg.aliexpress.com/sync', appkey ,appSecret)
            request = iop.IopRequest('aliexpress.affiliate.productdetail.get')
            request.add_api_param('product_ids', item_id)
            request.add_api_param('target_language', 'EN')
            request.add_api_param('tracking_id', '201010')
            response = client.execute(request)
            product = response.body['aliexpress_affiliate_productdetail_get_response']['resp_result']['result']['products']['product'][0]
            currentprice = product['target_app_sale_price']
            originalprice = product['target_original_price']
            name = product['product_title']
            request = iop.IopRequest('aliexpress.affiliate.link.generate')
            request.add_api_param('promotion_link_type', '0')
            request.add_api_param('source_values', itmurl)
            request.add_api_param('tracking_id', '201010')
            response = client.execute(request)
            try:
                link = response.body['aliexpress_affiliate_link_generate_response']['resp_result']['result']['promotion_links']['promotion_link'][0]['promotion_link']
            except:
                link = product['promotion_link']

            data = {
                "image": image.group(1) if image else None,
                "currentprice": currentprice,
                "originalprice": originalprice,
                "name": name,
                "link": link
            }
            return data
        else:
            return 'Invalid'
    except Exception as e:
        traceback.print_exc()
        return f'Some error occured: {e}'
        

print(get_details_by_item_id("https://www.aliexpress.com/i/1005006249903089.html"))
