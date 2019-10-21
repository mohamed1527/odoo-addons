{
    'name': 'News Application',
    'description': 'News Application.',
    'category': 'News',
    'author': 'Mohamed Ayman',
    'depends': ['base'],
    'application': True,
    'data': [

            'security/security.xml',
            'security/ir.model.access.csv',
             'views/article_view.xml',
             'views/news_menu.xml',
             'views/res_partner_view.xml',
             'views/tags_view.xml',
             'views/category_view.xml',
             'views/news_menu_tags.xml',
             'views/news_menu_category.xml',
             ]
}