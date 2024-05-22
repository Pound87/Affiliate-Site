import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import re, iop
import traceback
##from telegram import Bot
##ptb_bot =  Bot("6776802861:AAHZkeMDesnTTUVCFzx4GISMh7MdhzIU7MY")

appkey = 503784
appSecret = "cDKOdtBHzsQgC8bex7t0bw58zXhbWX89"


api_id = 29915391
api_hash = "b144e6d40501e4570a3a951fcf6a2ab4"
bot = Client('bot',api_id,api_hash,bot_token="6776802861:AAHZkeMDesnTTUVCFzx4GISMh7MdhzIU7MY")
user_client = Client('+212601608512',api_id,api_hash)
user_client.start()
# fill in your cookies and bot token here

COOKIES = 'ali_apache_id=33.22.97.119.1702571206893.324841.4; acs_usuc_t=x_csrf=trgm5s_zrkh_&acs_rt=222f2f82c1cb4a6289e1e0bb1f06682c; cna=yRoCHnpQonQCAXCGlBB1967H; xlly_s=1; ali_apache_track=; ali_apache_tracktmp=; e_id=pt90; _m_h5_tk=c85667aed53d388fe170b767cc5fba5b_1702573165531; _m_h5_tk_enc=4bbc02721c6174fed2e4f96c936d9da9; havana_tgc=NTGC_2d3dec3a640a56164d56ca162203886d; _hvn_login=13; x_router_us_f=x_alimid=1698006444; xman_us_t=x_lid=ma96439444ywcae&sign=y&rmb_pp=ayoub_ouahmane@outlook.fr&x_user=nbJdlllVzaBKNuztlZB/hWF3/rwtaQM1gb2Pn+9qLoQ=&ctoken=13fqs690el6id&l_source=aliexpress; aep_usuc_f=site=glo&b_locale=en_US&isb=y&x_alimid=1698006444&isfb=y; sgcookie=E100bwOevTBtoUdVEzRLDQdjc+bKOfM47u10wsVCJSNex6fD338gpxqBrXFnOJnpBKQadydYuzM8G/TeSZXLo4uKD/SgZyNbNddzcpR8J5mhfgY=; aep_common_f=qVyZymybe5+N9eIznxbPKecq9aKfdPsituE+0OsNDhv8YWZnb3OCiw==; xman_t=uWWPqO2JYcqloyL1KjCPiPg18oLW8tv0YJ2Lf/sYFwfDFbkXPVDWwYxSmBVZSkK1HUI0ftM15pOXQxYhJZ52+GAX1DRRTk5fvJUhdNTvNla/yHWh77330jAbUCSc9q/fNlHWaqf+r2DRIl0VxAy9H7EvCViAjloYlq2swEvOdflwANTYtae9OnZl3OcOf1YVw5q0NEXCRUw1w+5V44+fMf9pg9BOXchKOYQbTE+8fDgUqH5RXVJFsNMAbLpcjAwwwqn5SRvJA+pCtvHfIlEDjlrZuw910qaRGtCNvw+DJdLRJgq5WkNv1a7IdUuohqcsBZQf7qYQgS7c554Cvgs2bef9XsmqhkA/l1M/Kwcw0iEM65EQiXPI2WYPPmkuT0V1+O3glxu1byAHhmoSTb/3yZxq5TNn53EXqlX4/LTV4vdb1ylw2AcgAjMOgVuOrdY7ruROsK5Ru+9ppWV1X1pqq3CxzBuA0vsr/reUrSaksOO2mOUp2mer6FhaTKgptpdL9TvWS3vGSyEP/DvBNbsoPfmjGPgD0m8x1Rz0PZlGNa/21nhKlWeAoRFkYNqPTDlzHvYQbxSsJPRu67ZC34yBFS0Bps6pldo2EKaLR2pRhik4aqtT6hGhmSGb9v0UyGlmOQyi5ntQ4Z/FySJDHPp0R4VimRMjVKEdjGxhT8mCCHwyuAmwN4dLHJ2DQ90o+rw+zDBhb2q8Dk/ni7wdCh/3es17+yz6d8D6ACiVHzXZR9cNiO55h+nbkEUN7wwt3Km2; xman_f=xnq9Ri1yc/o1I8I27NLefDRVw69T5jACghblDAWuQuL/r4Wyf2doO5wYV7ofUA+xPaetRwA05Q8dndai2nOsdtOmPp2P1uD/ZRYIwJvZz4MXctRlyKRCXUy0Zn1AXt6BSdfia7tFAFY+TgawwvjtWQ71+ozmfK1HumBXJz0RbAJ7PooRgUjcXJOiuvBcBuBngho1rqD2Dt198GJvE/SF66r1JMNzro1nHScf5ugtDWZPNbTLaelAyQAGDSrh3QFRl88Mj2y13sdleNGjISyWM0V6K7VAkV4H54oLOzjUfFQh6O+aWKbhAx4ViBQACRiBEPLqjkeNjGdbHIjhPAC8zoixbZobliNkfja5LBAfZVHwY72BQH3JBfyUYPPcQHd6PAlSJVVIB0fxkQR4ETrTi8eUFuOFbbNz4FP4h5OTQyAGe00tMxEITqpDaLmctuon8zJV7irVKdq6EQlaBaUSTAYROw4aTIs8bexO2L/A1k8=; xman_us_f=x_l=0&x_user=MA|facebook|user|ifm|1698006444&x_lid=ma96439444ywcae&acs_rt=222f2f82c1cb4a6289e1e0bb1f06682c; x-hng=lang=en-US; JSESSIONID=F42C6640B7956405C98390429EC9A5AE; isg=BKOjlmsawvFQUo7F6foNfYKfMudNmDfao9JzStUA_4J5FMM2XWjHKoFGCvwar4_S; l=fBQQhsOgPc8JkSS2BOfaFurza77OSIRYYuPzaNbMi9fPOY1B5C05W1Ug_sY6C3MNF6P6R3S3hc2kBeYBqQAonxvtYQkvdpMmndLHR35..; tfstk=ed2X-Ibb-EYXZdADPZszRS8-dBH18r6eHhiTxlp2XxHYXPZ_viDZulH1frzB7VlNmV3tPP0qgxCD1Ca4XqoZ7sjsW4E3gGDYQPw_84zwQoy_ZdZ3j-SmQiD0mADO8wWF8oqmI2CghMWELaKCWw7FLTr0mADO8S8qMSjta8sjO2tLpHVFg4hjJo6kBdwWLjgLD49tq8ifS2ExPdpO4ZpERqtD13GHC0gFVgOMsKJsAPPdP2drM0mzLgsWlCcxq0gFVgOMsjno4XS5VEOG.'


headers = {
    "Cookie" : COOKIES,
    "Host":"portals.aliexpress.com"
}

product_details = {}

def get_item_id_from_url(product_url):
    pattern = r'/(\d+).html'
    match = re.search(pattern, product_url)
    if match:
        item_id = match.group(1)
        return item_id
    else:
        product_url = requests.get(product_url).url
        match = re.search(pattern, product_url)
        if match:
            item_id = match.group(1)
            return item_id
        else:
            product_url = requests.get(product_url).url
            match = re.search(pattern, product_url)
            if match:
                item_id = match.group(1)
                return item_id
            else:
                return None

async def get_details_by_item_id(itmurl):
    global product_details
    product_details = {}
    try:
        item_id = get_item_id_from_url(itmurl)
        if item_id:
            print(item_id)
            req = requests.get(f'https://www.aliexpress.com/item/{item_id}.html')
            image = re.search('<meta property="og:image" content="(.*?)"/>', req.text) if req else None
            product_details["image"] = image.group(1) if image else None
            print('i',image)

            client = iop.IopClient('https://api-sg.aliexpress.com/sync', appkey ,appSecret)



            request = iop.IopRequest('aliexpress.affiliate.link.generate')
            request.add_api_param('promotion_link_type', '0')
            request.add_api_param('source_values', itmurl)
            request.add_api_param('tracking_id', '201010')
            response = client.execute(request)
            try:
                link = response.body['aliexpress_affiliate_link_generate_response']['resp_result']['result']['promotion_links']['promotion_link'][0]['promotion_link']
            except:
                return " error: your affiliate account is unable to generate the affiliate link against your provided link"

            product_details["link"] = link
            
            request = iop.IopRequest('aliexpress.affiliate.productdetail.get')
            request.add_api_param('product_ids', item_id)
            request.add_api_param('target_language', 'EN')
            request.add_api_param('tracking_id', '201010')
            response = client.execute(request)
            try:
                product = response.body['aliexpress_affiliate_productdetail_get_response']['resp_result']['result']['products']['product'][0]
                currentprice = product['target_app_sale_price']
                originalprice = product['target_original_price']
                name = product['product_title']
            except:
                await user_client.send_message('@FNCOUPOS_bot',itmurl)
                return 'wait for bot message'

            product_details["currentprice"] = currentprice
            product_details["originalprice"] = originalprice
            product_details["name"] = name
            
            return product_details
        else:
            return 'Invalid'
    except Exception as e:        
        traceback.print_exc()
        return f'Some error occured: {e}'

def find_links(text):
    regex=r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
    pattern = re.findall(regex, text)
    return pattern[0]



@user_client.on_message(filters.photo & filters.user(['@FNCOUPOS_bot']))
async def forward(user_client, message):
    print('message from bot rcvd')
    msg_lines = message.caption.splitlines()
    text = 'تخفيض 🔥'
    for line in msg_lines:
        if "سعر التخفيض بالعملات : " in line:
            text = f"{text}\nالثمن بعد التخفيض 💸: {line.split('سعر التخفيض بالعملات : ')[-1]}"
            current_price = line.split('سعر التخفيض بالعملات : ')[-1]
        elif "إسم المنتج :" in line:
            text = f"{text}\n{line.split('إسم المنتج : ')[-1]}"
            name = line.split('إسم المنتج : ')[-1]
        elif "سعر العرض المحدود :" in line:
            original_price = line.split("سعر العرض المحدود :")[-1]
        elif "نسبة تخفيض المنتج بالعملات : " in line:
            discount_line = f"نسبة التخفيض 🔥 : _{line.split(':  ')[-1]}"
    text = f"{text}\n{discount_line}"
    text += (f"\nرابط المنتج 🎉: {product_details['link']}")
    image = product_details["image"]
    n_otext = f"🔥تخفيض: {name}\n\nالثمن بعد التخفيض 💵: {current_price}  ~~{original_price}~~\nرابط الشراء 🎉: {product_details['link']}"
    if image:
        rcvr_id= xx.chat.id
        await xx.delete()
        await bot.send_photo(-1002142475518 ,image,caption=n_otext, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('رابط المنتج', url=product_details['link'])]]))
        await bot.send_photo(rcvr_id ,image,caption=n_otext, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('رابط المنتج', url=product_details['link'])]]))
    else:
        rcvr_id= xx.chat.id
        photo = await user_client.download_media(message.photo.file_id)
        await xx.delete()
        await bot.send_photo(-1002142475518,photo,caption=n_otext, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('رابط المنتج', url=product_details['link'])]]))
        await bot.send_photo(rcvr_id, photo,caption=n_otext, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('رابط المنتج', url=product_details['link'])]]))


##@user_client.on_message(filters.user([5587063896]))
##async def reply(user_client, message):
##    print(message.photo)
##    print(message.photo.file_id)
##    await ptb_bot.send_photo(-1002142475518 ,photo=message.photo.file_id,caption='hello')

##    await bot.send_photo(5587063896 ,photo="AgACAgQAAxkBAAIBemWO7_zvN_GiYFsqtMhl1wPe7vvEAAL9yDEb5I54UB1sO5KOdnxDAQADAgADeQADNAQ")

@bot.on_message(filters.command('start'))
async def start(pyro_client, message):
    await message.reply_text("Hello, I'm a bot to get the best discount on AliExpress. Send me the link of the product you want to get the discount.")

@bot.on_message(filters.text & filters.regex(r'.*aliexpress.*') & filters.user([6212762417,1467358214,5587063896]))
async def get_details(pyro_client, message:Message):
    ul = find_links(message.text)
    if ul:
        global xx
        xx = await message.reply_text('Please wait...')
        details = await get_details_by_item_id(ul)
        if details:
            if details == 'Invalid':
                await xx.delete()
                await message.reply_text('Invalid link! please send a valid link.')
            elif 'error' in details:
                await message.reply_text(str(details))
            elif 'wait' in details:
                return
            else:
                image = details['image']
                current_price = details['currentprice']
                original_price = details['originalprice']
                name = details['name']
                link = details['link']
                if image:
                    await xx.delete()
                    await bot.send_photo(-1002142475518 ,image,caption=f"🔥تخفيض: {name}\n\nالثمن بعد التخفيض 💵: {current_price}$  ~~{original_price}$~~\nرابط الشراء 🎉: {link}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('رابط المنتج', url=link)]]))
                    await message.reply_photo(image, caption=f"🔥تخفيض: {name}\n\nالثمن بعد التخفيض 💵: {current_price}$  ~~{original_price}$~~\nرابط الشراء 🎉: {link}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('رابط المنتج', url=link)]]))
                else:
                    await xx.delete()
                    await bot.send_message(-1002142475518,f"🔥تخفيض: {name}\n\nالثمن بعد التخفيض 💵: ${current_price}  ~~${original_price}~~\nرابط الشراء 🎉: {link}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('رابط المنتج', url=link)]]))
                    await message.reply_text(f"🔥تخفيض: {name}\n\nالثمن بعد التخفيض 💵: {current_price}$  ~~{original_price}$~~\nرابط الشراء 🎉: {link}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('رابط المنتج', url=link)]]))
        else:
            await xx.delete()
            await message.reply_text('Invalid link! please send a valid link.')
    else:
        return

bot.run()
user_client.run()
