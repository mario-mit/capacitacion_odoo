# -*- coding: utf-8 -*-

{
    'name': "space_mision",
    
    'summary': """Space travel app to journey to the moon""",
    
    'description': """
        Space travel app to manage:
        - space ship
        - crew
    """,
    
    'author': "M",
    
    'webside': "https://m.com",
    
    'category': "Space",
    
    'version': "0.2",
    
    'depends': ['base'],
    
    'data': [
        'security/space_mision_security.xml',
        'security/ir.model.access.csv',
        'views/space_mision_menuitem.xml',
        'views/space_mision_views.xml'
    ],
    
    'demo': [
        'demo/space_mission_demo.xml'
    ]
}
