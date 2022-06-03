# -*- coding: utf-8 -*-
{
    'name': 'lgps_notifications',
    'description': 'Intralix module for record offline notifications',
    'author': 'Intralix',
    'license': "AGPL-3",
    'website': 'https://www.intralix.com',
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': [
        'base',
        'lgps'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/offline_notification_menu.xml',
        'views/offline_gpsdevice.xml',
        'views/offline_notification_rules.xml',
        'views/offline_client_configuration.xml',
        'views/offline_notifications.xml',
        'reports/email_preview.xml',
        'data/cron_task.xml',
    ],
}
