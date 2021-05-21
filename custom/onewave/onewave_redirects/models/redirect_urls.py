from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

import requests

class RedirectUrls(http.Controller):
    @http.route(['/eventos/registro/<string:event_id>'], type='http', auth="public", website=True, csrf=False)
    #next controller with url for submitting data from the form#
    def customer_form_submit(self, event_id, **post):
        _logger.info('***************************************************************')
        _logger.info('***************************************************************')

        _logger.info('***************************************************************')

        event = request.env['event.event'].sudo().search([('id', '=', int(event_id))])
        user = request.env['res.users'].sudo().browse([request.session.uid])

        _logger.info(event_id)
        return request.render("onewave_redirects.registro-completado", {'event': event, 'attendee': user})
