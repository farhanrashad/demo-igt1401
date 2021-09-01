# -*- coding: utf-8 -*-

{
    "name": "General Ledger Report",
    'version': '14.0.0.2',
    "category": 'Accounting',
    "summary": 'General Ledger Report',
    'sequence': 1,
    "description": """"General Ledger Report """,
    "author": "Dynexcel",
    "website": "https://www.dynexcel.com",
    'depends': ['stock_account','report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        'reports/report_general_ledger.xml',
        'wizards/report_genral_ledger_wizard_views.xml',
        #'views/view_stock_transfer_order.xml',
        
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}

