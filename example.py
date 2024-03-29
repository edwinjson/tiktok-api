from signer import Argus, Ladon, Gorgon, md5
from urllib.parse import urlencode
import time, random
import requests

def get_Signature (params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "v04.04.05-ov-android", sdk_version: int = 134744640, platform: int = 0, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        if not unix: unix = int(time.time())
    
        return Gorgon(params, unix, payload, cookie).get_value() | { 
            "x-ladon"   : Ladon.encrypt(unix, license_id, aid),
            "x-argus"   : Argus.get_sign(params, x_ss_stub, unix,
                platform        = platform,
                aid             = aid,
                license_id      = license_id,
                sec_device_id   = sec_device_id,
                sdk_version     = sdk_version_str, 
                sdk_version_int = sdk_version
            )
        }

def get_devices():
     devices = open("./utils/devices.txt", "r").read().splitlines()
     device = eval(random.choice(devices))

     return device

def tiktok_follow(user_id, sec_user_id):
    device = get_devices()
    print(device['device_id'])
    # urlQuery = urlencode(device)

    urlQuery = "user_id="+user_id+"&sec_user_id="+sec_user_id+"&type=1&channel_id=0&from=13&from_pre=13&item_id=7094730482549558570&enter_from=homepage_hot&action_time=1708456737042&is_network_available=true&iid="+device['install_id']+"&device_id="+device['device_id']+"&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=320706&version_name=32.7.6&device_platform=android&os=android&ab_version=32.7.6&ssmix=a&device_type=MI+5s&device_brand=Xiaomi&language=en&os_api=26&os_version=8.0.0&openudid=94e04b4ae3020c26&manifest_version_code=2023207060&resolution=1080*1920&dpi=480&update_version_code=2023207060&_rticket=1708456737056&is_pad=0&current_region=US&app_type=normal&sys_region=US&timezone_name=America%2FLos_Angeles&residence=US&app_language=en&ac2=wifi5g&uoo=0&op_region=US&timezone_offset=-28800&build_number=32.7.6&host_abi=arm64-v8a&locale=en&region=US&ts=1708456766&cdid=4898160d-034d-48d0-a605-b198b9ab502e"

    url = "https://api16-normal-useast5.us.tiktokv.com/aweme/v1/commit/follow/user/?" + urlQuery

    payload = {}


    res = get_Signature(urlQuery)

    headers = {
    'x-tt-multi-sids': '7289379146936861742%3A7015b5b61af5259e62fb9834fa2dc5ed%7C7289378818065843246%3Ad33529cae776bb3f253bda9787f7b73a',
    'sdk-version': '2',
    'x-bd-kmsv': '0',
    'X-Tt-Token': 'your token',
    'x-bd-client-key': '#CyGLqgQxFhj/nXQ42XTZHwjhjGHdgxBGrfSYb8F3dokZEk2fEeEopWqnpIGBCtXF/k46TjXqJJP2m5jj',
    'multi_login': '1',
    'passport-sdk-version': '19',
    'x-tt-dm-status': 'login=1;ct=1;rt=1',
    'x-vc-bdturing-sdk-version': '2.3.4.i18n',
    'x-tt-store-region': 'us',
    'x-tt-store-region-src': 'uid',
    'User-Agent': 'com.zhiliaoapp.musically/2023207060 (Linux; U; Android 8.0.0; en; MI 5s; Build/OPR1.170623.032;tt-ok/3.12.13.4-tiktok)',
    'X-SS-REQ-TICKET': res['x-ss-req-ticket'],
    'X-Ladon': res['x-ladon'],
    'X-Khronos': res['x-khronos'],
    'X-Argus': res['x-argus'],
    'X-Gorgon': res['x-gorgon'],
    'Host': 'api16-normal-useast5.us.tiktokv.com',
    'Cookie': 'your cookie'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response)
    print(response.text)
    # print(response.content)
    return response

def tiktok_digg(aweme_id):
    urlQuery = "aweme_id="+aweme_id+"&enter_from=homepage_hot&friends_upvote=false&type=1&channel_id=0&iid=7339107689308079903&device_id=7319450450397906475&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=330403&version_name=33.4.3&device_platform=android&os=android&ab_version=33.4.3&ssmix=a&device_type=MI+5s&device_brand=Xiaomi&language=en&os_api=26&os_version=8.0.0&openudid=94e04b4ae3020c26&manifest_version_code=2023304030&resolution=1080*1920&dpi=480&update_version_code=2023304030&_rticket=1708781003509&is_pad=0&current_region=US&app_type=normal&sys_region=US&timezone_name=America%2FLos_Angeles&residence=US&app_language=en&ac2=wifi5g&uoo=0&op_region=US&timezone_offset=-28800&build_number=33.4.3&host_abi=arm64-v8a&locale=en&region=US&ts=1708781032&cdid=4898160d-034d-48d0-a605-b198b9ab502e"
    url = "https://api16-normal-useast5.us.tiktokv.com/aweme/v1/commit/item/digg/?" + urlQuery

    res = get_Signature(urlQuery)

    payload = {}

    headers = {
    'x-tt-multi-sids': '7289379146936861742%3A7015b5b61af5259e62fb9834fa2dc5ed%7C7289378818065843246%3Ad33529cae776bb3f253bda9787f7b73a%7C7325086086252905518%3Aa08c5ce7bb5f2f3e2b7ea27177c43b6c',
    'sdk-version': '2',
    'x-bd-kmsv': '0',
    'x-tt-dm-status': 'login=1;ct=1;rt=1',
    'X-Tt-Token': 'yout token',
    'x-bd-client-key': '#1Tqwdw4Dg/WG+iWms7LxC5OOWfc4Ns9willeO1CGuH2dMorH6yi+XHIGWKTiDUhwFphOWnFhY0tZzbmQ',
    'multi_login': '1',
    'x-opti-ut': 'ClH4hLiYRSUWg2k0lHOVErlmGWQyOSXlDQ7hnAR6WNHrQdQGSnM-wPiIlU0l1vaLKVfcnatS40su9_CN26PP7CAxFLhvCN65Vglxa1-q4RCL59caSQo800KFBvXVIs3E4iir1JFGRqf_edv1PO2A0x9cONrrGtmEuJWD656BcGLq5jDSFrjTduKDWSfVhnrBskkNEJWgyg0Yi9bl1woiAQR2CfHa',
    'passport-sdk-version': '19',
    'pns_event_id': '121',
    'x-vc-bdturing-sdk-version': '2.3.6.i18n',
    'x-tt-store-region': 'us',
    'x-tt-store-region-src': 'uid',
    'User-Agent': 'com.zhiliaoapp.musically/2023304030 (Linux; U; Android 8.0.0; en; MI 5s; Build/OPR1.170623.032;tt-ok/3.12.13.4-tiktok)',
    'X-SS-REQ-TICKET': res['x-ss-req-ticket'],
    'X-Ladon': res['x-ladon'],
    'X-Khronos': res['x-khronos'],
    'X-Argus': res['x-argus'],
    'X-Gorgon': res['x-gorgon'],
    'Host': 'api16-normal-useast5.us.tiktokv.com',
    'Cookie': 'your cookie'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    return response
    
def get_tiktok_video_comments(aweme_id, cursor, count):
    t = time.time()
    ts = int(t)

    urlQuery = "aweme_id=7305007123568610592&cursor=0&count=8&forward_page_type=1&channel_id=0&user_avatar_shrink=96_96&ad_pricing_type=0&load_type=0&offline_pin_comment=1&author_relation_type=0&scenario=0&enter_from=homepage_hot&repost_insert_ids&is_non_personalized=false&suggest_words=%7B%22suggestWordsList%22%3A%5B%7B%22suggestWord%22%3A%5B%7B%22word%22%3A%22auto+accessories%22%7D%5D%2C%22scene%22%3A%22feed_bar%22%7D%5D%7D&shown_cnt=2730&iid=7319451158773335851&device_id=7319450450397906475&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=320706&version_name=32.7.6&device_platform=android&os=android&ab_version=32.7.6&ssmix=a&device_type=MI+5s&device_brand=Xiaomi&language=en&os_api=26&os_version=8.0.0&openudid=94e04b4ae3020c26&manifest_version_code=2023207060&resolution=1080*1920&dpi=480&update_version_code=2023207060&_rticket=1704601169688&is_pad=0&current_region=US&app_type=normal&sys_region=US&timezone_name=America%2FLos_Angeles&residence=US&app_language=en&ac2=wifi5g&uoo=0&op_region=US&timezone_offset=-28800&build_number=32.7.6&host_abi=arm64-v8a&locale=en&region=US&ts="+str(ts)+"&cdid=4898160d-034d-48d0-a605-b198b9ab502e&is_landscape=0"

    res = get_Signature(urlQuery)

    url = "https://api16-normal-useast8.us.tiktokv.com/aweme/v2/comment/list/?" + urlQuery

    payload = {}
    headers = {
    'Accept-Encoding': 'gzip',
    'x-tt-app-init-region': 'carrierregion=;mccmnc=;sysregion=US;appregion=US',
    'x-tt-multi-sids': '7289378818065843246%3Acb3465f53353502fde3ea16e61aec936%7C7289379146936861742%3A7015b5b61af5259e62fb9834fa2dc5ed',
    'check_preload': 'true',
    'sdk-version': '2',
    'traceparent': 'unsampled_ttk_trace_span_76717-00',
    'x-bd-kmsv': '0',
    'x-bd-client-key': '#CyGLqgQxFhj/nXQ42XTZHwjhjGHdgxBGrfSYb8F3dokZEk2fEeEopWqnpIGBCtXF/k46TjXqJJP2m5jj',
    'multi_login': '1',
    'passport-sdk-version': '19',
    'x-tt-dm-status': 'login=1;ct=1;rt=1',
    'x-vc-bdturing-sdk-version': '2.3.4.i18n',
    'x-tt-store-region': 'us',
    'x-tt-store-region-src': 'uid',
    'User-Agent': 'com.zhiliaoapp.musically/2023207060 (Linux; U; Android 8.0.0; en; MI 5s; Build/OPR1.170623.032;tt-ok/3.12.13.4-tiktok)',
    'X-SS-REQ-TICKET': res['x-ss-req-ticket'],
    'X-Ladon': res['x-ladon'],
    'X-Khronos': res['x-khronos'],
    'X-Argus': res['x-argus'],
    'X-Gorgon': res['x-gorgon'],
    'Host': 'api16-normal-useast8.us.tiktokv.com',
    'Connection': 'Keep-Alive',
    'Cookie': 'odin_tt=3d414f2af95b39318ac0baace099d883782281702e111d89f8f913fd4564e32a775e9213225e78a1e50fad1a690a6f7fab545ef1cab9f3101792ea1010d629f7f62af8c02835a8b6b15c453bd0750f13'
    }

    proxys  = {
                "http": "http://192.177.98.101:9847",
                "https": "http://192.177.98.101:9847"
            }
    response = requests.request("GET", url, headers=headers, data=payload,proxies=proxys)
    # response = requests.request("GET", url, headers=headers, data=payload)

    return response.text
    # print(response.text)

if __name__ == '__main__':
    
    videoComents = get_tiktok_video_comments("7305007123568610592", "0", "10")
    print(videoComents)

    tiktok_digg("7305217874866621704")

    tiktok_follow("7337318108808857000", "MS4wLjABAAAAj7kGC4Kk-1gMAOIpLStGjmFjAREam8yEy1MIahFA_tngDTl0GS_-tCdAH1FAI9Wu")
