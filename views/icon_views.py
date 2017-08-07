from urllib.parse import unquote, urlparse
from sanic.response import json
from sanic import Blueprint

from lxml import html
import aiohttp

bp = Blueprint('icon_blueprint')


@bp.route('/')
async def icon(request):
    def is_image_response(response):
        return 300 > response.status >= 200 and 'image' in response.headers.get('Content-Type')

    url = request.args.get('url')
    if not url:
        return json({})
    url = unquote(url)
    o = urlparse(url)
    url_base = f'{o.scheme}://{o.netloc}'
    # 先取favicon
    favicon_url = f'{url_base}/favicon.ico'

    conn = aiohttp.TCPConnector(verify_ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(favicon_url) as resp:
            if is_image_response(resp):
                return json({"url": favicon_url})

        # 解析HTML
        async with session.get(url) as resp:
            tree = html.fromstring(await resp.text())
            link_tree = tree.xpath('/html/head/link')
            for link_dom in link_tree:
                if 'icon' in link_dom.attrib.get('rel'):
                    favicon_url = link_dom.get('href')
                    if not favicon_url.startswith('http'):
                        favicon_url = f'{url_base}{favicon_url}'
                        async with session.get(favicon_url) as resp:
                            if is_image_response(resp):
                                return json({"url": favicon_url})

    return json({})