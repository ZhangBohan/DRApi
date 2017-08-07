from sanic import Sanic
from sanic.response import json

from views.icon_views import bp as icon_bp

app = Sanic()
app.blueprint(icon_bp)


@app.route("/")
async def test(request):
    return json({"hello": "world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)