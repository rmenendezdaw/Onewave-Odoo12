#-*- coding: utf-8 -*-
import logging

from odoo import fields, models
_logger = logging.getLogger(__name__)


class AddGroup(models.Model):
    _inherit = "event.event"

    grupos = fields.Many2many(comodel_name = "res.users", string='Añadir grupos', domain="[('tipo', '=', 'Grupo')]")
    channel_id = fields.Many2one(comodel_name="mail.channel", string="Canal de chat")
    ubicacion = fields.Char(string="Ubicación")
    def send_mail_to_groups(self):

        for item in self.grupos:
            # Crea socios para el administrador
            id_channel_org = self.env['mail.channel.partner'].create({
                    'partner_id': self.user_id.partner_id.id
            })
            # Crea socios para los grupos del evento
            id_channel_partner = self.env['mail.channel.partner'].create({
                'partner_id': item.partner_id.id
            })
            #Crea el canal privado para cada uno de los grupos con el organizador
            id_channel = self.env['mail.channel'].sudo().create({
                'name': self.name+"-"+item.partner_id.name,
                'public': 'private',
                'channel_last_seen_partner_ids': [(6, 0, [id_channel_partner.id, id_channel_org.id])]
            })
            #Diccionario para el mensaje
            dicctionary = {
                'subject': self.name,
                'email_from': self.user_id.login, 
                'author_id': self.user_id.partner_id.id,
                'model': 'mail.channel',
                'message_type': 'comment',
                'record_name': 'EVENTO',
                'subtype_id': self.env.ref('mail.mt_comment').id,
                'body': '¿Quieres unirte al evento '+ self.name +'?!',
                'partner_ids': [(6, 0, [item.partner_id.id, self.user_id.partner_id.id])],
                'moderation_status': 'accepted',
                'res_id': '200',
                'channel_ids': [(4, id_channel.id)]
            }
            # Crea el mensaje para los grupos 
            aux = self.env['mail.message'].sudo().create(dicctionary)

            try:
                mail = self.env['mail.mail']
                values={
                    'display_name': self.env.user.name,
                    'email_from': self.env.user.email,
                    'author_id': self.env.user.id,
                    'email_to': item.email,
                    'subject': 'Evento de OneWave',
                    'body_html': f'<p><strong>{self.env.user.name}</strong> quiere que te unas a su evento "{self.name}" </p>'
                }
                msg_id = mail.sudo().create(values)
                _logger.info(values)
                if msg_id:
                    msg_id.send()
            except:
                _logger.info("Try catch error!")