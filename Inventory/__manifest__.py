{
    'name':'Inventory_Audit',
    'version' : '1.1',
    'author': 'weblearns',
    'summary' :'Inventory Audit',
    'sequence' : 1,
    'description' : "Inventory Audit"
                    "odoo v15",
    'category' : 'Inventory Audit',                
    'website' : 'https://freeweblearns.blogspot.com',
    'depends': ['base'],
    'data' : [
        'views/schedule.xml',
        'views/phase.xml',
        'views/locations.xml',
        'views/items.xml',
        'views/actual_stock.xml',
        'views/scanned_data.xml',
        'views/data.xml',
        'security/ir.model.access.csv',
        'security/security.xml'
    ]

}