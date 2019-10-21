{
    'name': 'To-Do Application',
    'description': 'Mange personal to-do tasks.',
    'author': 'M.Ayman',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
        'views/todo_menu.xml',
        'views/todo_view.xml',
        'views/res_partner_view.xml',
        'views/index_template.xml',
    ],
}
