# Copyright 2019 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'
    
    cargo = fields.Selection(string="cargo", selection=[('par', 'Particular'),('ger', 'Gerente'),('resp', 'Responsable'),('pres', 'Presidente')])
    carrera = fields.Selection(string="carrera", selection=[('Indie', 'Indie'),('Profesional', 'Profesional')])
    especialidad = fields.Selection(string="especialidad", selection=[('Acustico', 'Acústico'),('Electrico', 'Eléctrico')])
    tipo = fields.Selection(string="Tipo", selection=[('Grupo', 'Grupo'),('Organizador', 'Organizador')])

    