# -*- coding: utf-8 -*-

{
    'name': "library management",
    
    'summary': "Library management app",
    
    'description': """
        Library management app to help to manage:
        - clients
        - books
        - lendings
    """,
    
    'author': "M",
    
    'website': "https://m.com",
    
    'category': "Libraries",
    
    'version': "0.1",
    
    'depends': ['base'],
    
    'data':[
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_admin_menuitem.xml'
    ],
    
    'demo':[
        'demo/library_admin_demo.xml'
    ]
    
}
