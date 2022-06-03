# -*- coding: utf-8 -*-
{
    'name': 'lgps',
    'description': 'Intralix module for internal processes',
    'author': 'Intralix',
    'application': True,
    'license': "AGPL-3",
    'website': 'https://www.intralix.com',
    'category': "Services/Intralix",
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
        'wizard/assign_accessories_wizard.xml',
        'wizard/accessories_operations_wizard.xml',
        'wizard/devices_operations_wizard.xml',
        'wizard/mass_device_comment_wizard.xml',
        'views/main_menu.xml',
        'views/res_config_settings_views.xml',
        'views/cellchip.xml',
        'views/accessory.xml',
        'views/gpsdevice.xml',
        'views/platform_list.xml',
        'views/subscription.xml',
        'views/tickets.xml',
        'views/dolar_history.xml',
        'views/helpdesk_custom_form_view.xml',
        'views/helpdesk_custom_tree_view.xml',
        'views/task_custom_form_view.xml',
        'views/accessory_history.xml',
        'views/device_history.xml',
        'views/partner.xml',
    ],
}
