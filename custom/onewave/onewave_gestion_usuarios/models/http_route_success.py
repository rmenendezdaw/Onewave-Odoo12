from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

import requests

class SuccessForm(http.Controller):
    @http.route(['/organizador/form/success'], type='http', auth="public", website=True, csrf=False)
    #next controller with url for submitting data from the form#
    def customer_form_submit(self, **post):
        return request.render("onewave_gestion_usuarios.tmp_customer_form_success")
