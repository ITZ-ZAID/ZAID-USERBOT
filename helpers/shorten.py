import aiohttp
from yourls import YOURLSClient
from yourls.exceptions import YOURLSURLExistsError, YOURLSKeywordExistsError


YOURLS_URL = None
YOURLS_KEY = None


async def shorten_url(url, keyword):
    if not YOURLS_URL or not YOURLS_KEY:
        return "API ERROR"

    url_checked = await url_check(url)
    if url_checked:
        yourls = YOURLSClient(YOURLS_URL, signature=YOURLS_KEY)
        try:
            shorturl = yourls.shorten(url, keyword).shorturl
            result = shorturl
        except (YOURLSURLExistsError, YOURLSKeywordExistsError):
            result = "KEYWORD/URL Exists"
    else:
        result = "INVALID URL"
    return result


async def url_check(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return resp.status == 200
    except aiohttp.ClientError:
        return False
