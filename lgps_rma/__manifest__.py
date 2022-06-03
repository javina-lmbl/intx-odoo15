# -*- coding: utf-8 -*-
{
    'name': 'lgps_rma',
    'description': 'Intralix module for track rma process with providers',
    'author': 'Intralix',
    'license': "AGPL-3",
    'website': 'https://www.intralix.com',
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': [
        'base',
        'lgps',
        'mail'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/rma_done_mail_template.xml',
        'views/rma_process_menu.xml',
        'views/rma_process.xml',
        'views/rma_gpsdevice.xml'
    ],
}
