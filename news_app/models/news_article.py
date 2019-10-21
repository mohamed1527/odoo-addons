from odoo import fields, models


class NewsArticle(models.Model):
    _name = 'news.article'
    _description = 'article information'
    _rec_name = 'title'
    title = fields.Char('Article Title', required=True)
    date = fields.Date('Date')
    body = fields.Html('Body')
    author_ids = fields.Many2many('res.partner', string='Author')
    thumbnail = fields.Binary('Thumbnail')
    summary = fields.Text('Summary')
    category_id = fields.Many2one('news.category', string='Category')
    tags_ids = fields.Many2many('news.tags', string='Tags')
