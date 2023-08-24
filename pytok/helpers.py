from .exceptions import *

import re


def extract_tag_contents(html):
    if next_json := re.search(
        r"id=\"__NEXT_DATA__\"\s+type=\"application\/json\"\s*[^>]+>\s*(?P<next_data>[^<]+)",
        html,
    ):
        nonce_start = '<head nonce="'
        nonce_end = '">'
        nonce = html.split(nonce_start)[1].split(nonce_end)[0]
        return html.split(
            f'<script id="__NEXT_DATA__" type="application/json" nonce="{nonce}" crossorigin="anonymous">'
        )[1].split("</script>")[0]
    else:
        if sigi_json := re.search(
            '<script id="SIGI_STATE" type="application\/json">(.*?)<\/script>',
            html,
        ):
            return sigi_json.group(1)
        else:
            raise CaptchaException(
                "TikTok blocks this request displaying a Captcha \nTip: Consider using a proxy or a custom_verify_fp as method parameters"
            )


def extract_video_id_from_url(url):
    url = requests.head(url=url, allow_redirects=True).url
    if "@" in url and "/video/" in url:
        return url.split("/video/")[1].split("?")[0]
    else:
        raise TypeError(
            "URL format not supported. Below is an example of a supported url.\n"
            "https://www.tiktok.com/@therock/video/6829267836783971589"
        )

def extract_user_id_from_url(url):
    url = requests.head(url=url, allow_redirects=True).url
    if "@" in url and "/video/" in url:
        return url.split("/video/")[0].split("@")[1]
    else:
        raise TypeError(
            "URL format not supported. Below is an example of a supported url.\n"
            "https://www.tiktok.com/@therock/video/6829267836783971589"
        )

def add_if_not_replace(text, pat, replace, add):
    if re.search(pat, text):
        return re.sub(pat, replace, text)
    text += add
    return text

