# -*- coding: utf-8 -*-
{
    'name': "Task Workflow",
    'summary': """
        Task Workflow through stages
        """,
    'description': """
        Project Task Workflow
    """,
    'author': "Dynexcel",
    'website': "http://www.dynexcel.com",
    'category': 'Project',
    'version': '14.0.0.3',
    "price": 75,
    "currency": "USD",
    'depends': ['project'],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_data.xml',
        'views/project_views.xml',
    ],
    "auto_install": False,
    "installable": True,
    "live_test_url":'https://www.youtube.com/watch?v=2A6UAiSnpW0',
    "images":['static/description/banner.jpg'],
}
