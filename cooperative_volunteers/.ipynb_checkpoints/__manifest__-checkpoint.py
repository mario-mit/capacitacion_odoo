# -*- coding: utf-8 -*-

{
    'name': "Cooperative Volunteers",
    
    'summary': "Cooperative Volunteers app to manage sales",
    
    'description': """
        Cooperative Volunteers app to help to manage:
        - products
        - sales
    """,
    
    'author': "M",
    
    'website': "https://m.com",
    
    'version': "0.1",
    
    'category': "Volunteers",
    
    'depends':['base'],
    
    'data': [
        'security/coop_volunteers_security.xml',
        'security/ir.model.access.csv'
    ],
    
    'demo':[
        'demo/coopera_volunteers_demo.xml',
    ]
}
