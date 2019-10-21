from odoo import fields, models


class NewsCategory(models.Model):
    _name = 'news.category'
    _description = 'category information'
    _rec_name = 'category_title'
    category_title = fields.Char('CategoryTitle', required=True)
    article_ids = fields.One2many('news.article', 'category_id', string='Articles')
