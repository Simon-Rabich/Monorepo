import requests
from requests import Response
from typing import List
import json

HEADERS : dict = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate",
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "cache-control": "no-cache",
        "cookie": 'personalization_id="v1_gUtOzS7RUaDYuoBu0okEiA=="; guest_id=v1%3A160369966909909677; _ga=GA1.2.2110928152.1603699671; kdt=FxFyjblskstePNG2XHSPaRMdgTtGMgczVNhvaUVo; auth_token=9b2a9fa3a7e32c911412fb11796fff3483ae62ac; ct0=67269e31e2bf4614493c1f1ac38390f3bd0b8ffcfde7b5393d1bf24551f336be771277964017da5e499a251e052c7735324d2b484bd88a075171ac59294f51b5576b8cfb03bc2a105caf339354e77d43; des_opt_in=Y; twid=u%3D1320638673797500928; _gid=GA1.2.746981199.1618042046; lang=en; at_check=true; external_referer=padhuUp37zixoA2Yz6IlsoQTSjz5FgRcKMoWWYN3PEQ%3D|0|8e8t2xd8A2w%3D; mbox=PC#1035d4e9e71d40d5836e2e4af1a42e1e.37_0#1681292610|session#9c1a791453ad4aff90a539662fc4db7f#1618049537',
        "pragma": "no-cache",
        "x-csrf-token": "67269e31e2bf4614493c1f1ac38390f3bd0b8ffcfde7b5393d1bf24551f336be771277964017da5e499a251e052c7735324d2b484bd88a075171ac59294f51b5576b8cfb03bc2a105caf339354e77d43",
        "x-twitter-active-user": "yes",
        "x-twitter-auth-type": "OAuth2Session",
        "x-twitter-client-language": "en"
    }

URI: str = 'https://twitter.com/i/api/2/timeline/conversation/{}.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&send_error_codes=true&simple_quoted_tweet=true&count=20&include_ext_has_birdwatch_notes=false&ext=mediaStats%2ChighlightedLabel'


def get_data_from_web(status_id: str):

    res: Response = requests.get(URI.format(status_id), headers=HEADERS)

    if res.status_code == 200:

        comments: List[dict] = []

        text = ''

        global_objects = json.loads(res.text)['globalObjects']

        tweets: dict = global_objects['tweets']

        users: dict = global_objects['users']

        for k, v in tweets.items():

            if k != status_id:

                user_id_str = tweets[k]['user_id_str']

                comments.append({"name": users[user_id_str]['name'], "screen_name": users[user_id_str]['screen_name'],
                                 "full_text": tweets[k]['full_text'], "created_at": tweets[k]['created_at']})

            if k == status_id:

                user_id_str = tweets[k]['user_id_str']

                text = str({"status_id": status_id, "full_text": tweets[k]['full_text'],
                        "name": users[user_id_str]['name'],
                        "screen_name": users[user_id_str]['screen_name'],
                        "created_at": tweets[k]['created_at']
                        })


        return text, str(comments)

