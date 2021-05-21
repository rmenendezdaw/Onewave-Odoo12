# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

import requests
class GroupForm(http.Controller):
    @http.route(['/grupo/form/submit'], type='json', auth="public", website=True, csrf=False)
    #next controller with url for submitting data from the form#
    def custom_form_submit(self, **post):
        
        diccionario = {
            'name': post.get('name'),
            'email': post['email'],
            'login': post.get('email'),
            'display_name': post.get('name_group'),
            'phone': post.get('phone'),
            'carrera': post.get('carrera'),
            'especialidad': post.get('especialidad'),
            'tipo': 'Grupo',
            'active': False
        }

        try:
            user = request.env['res.users'].sudo().create(diccionario)

            grupo = request.env['res.groups'].sudo().browse([45])
            grupo.sudo().users = [(4, user.id)]
            
            aux = requests.post(
            "https://api.mailgun.net/v3/sandbox1d3bd881e9834a108a7ddf26708204f5.mailgun.org/messages",
            auth=("api", "APIMAILGUN"),
            data={"from": "One Wave <onewave@onewave.es>",
                "to": ["onewave@onewave.es"],
                "subject": f"{post.get('name')} ha solicitado darse de alta",
                "text": f"Hola! \nHemos recibido la solicitud de un grupo con el siguiente email {post.get('email')} revisadlo en el panel de Odoo!"})

            return {'result': 'True'}
        except:
            return {'result': 'False'}
