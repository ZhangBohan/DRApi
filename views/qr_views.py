from io import BytesIO

from sanic.response import raw
from sanic import Blueprint
from sanic.views import HTTPMethodView

import qrcode

bp = Blueprint('qr_blueprint')


class QrView(HTTPMethodView):

    def get(self, request):
        return self.data_to_qr_reponse(request.args.get('data'))

    def post(self, request):
        return self.data_to_qr_reponse(request.body)

    @classmethod
    def data_to_qr_reponse(cls, data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        io = BytesIO()
        img.save(io)
        content = io.getvalue()
        io.close()
        return raw(content, content_type='image/jpeg')

bp.add_route(QrView.as_view(), '/')