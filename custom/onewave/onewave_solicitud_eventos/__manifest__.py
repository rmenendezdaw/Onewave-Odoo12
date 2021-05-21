# © 2018 Creu Blanca
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Onewave Solicitud Eventos',
    'version': '12.0.1.0.0',    
    'license': 'AGPL-3',
    'summary': 'Lógica para añadir grupos a eventos.',
    'author': 'Raul',    
    'depends': [
        'event',
        'base',
        'mail'
    ],
    'data': [
        'views/add_group.xml'
    ],    
    #'images': ['images/sshot-wizard1.png'],
    'installable': True,
}
