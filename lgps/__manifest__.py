# -*- coding: utf-8 -*-
{
    'name': 'lgps',
    'description': 'Intralix module for internal processes',
    'author': 'Intralix',
    'application': True,
    'website': 'https://www.intralix.com',
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': [
        'base',
        'stock',
        'contacts',
        'account',        
        'crm',
        'sale_subscription',
        'helpdesk',
        'mail',
        'project',
        'sale'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/main_menu.xml',
        'views/cellchip.xml',
        'views/accessory.xml',
        'views/gpsdevice.xml',
        'views/platform_list.xml',
        'views/subscription.xml',
        'views/tickets.xml',
    ],
}
