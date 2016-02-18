
# -*- coding: utf-8 -*-
{
    'name': "reporting custum soulco",

    'summary': """Design Odoo for Soulco Client Reports""",

    'description': """ Reporting for Soulco project """,

    'author': "IGPro",
    'website': "http://igpro-online.com",
    'category': 'Product',
    'version': '0.1',

    'depends': ['sale','stock','purchase'],

    'data': [
        'views/serial_quotation_report.xml',
        'views/serial_purchase_order_report.xml',
        'views/serial_reporting_picking_custum.xml',
    ],

}
