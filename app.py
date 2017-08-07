from sanic import Sanic
from sanic.response import json

from views.icon_views import bp as icon_bp
from views.qr_views import bp as qr_bp

app = Sanic()
app.blueprint(icon_bp, url_prefix='/icon')
app.blueprint(qr_bp, url_prefix='/qrcode')


@app.route("/")
async def test(request):
    return json({"hello": "world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=4)