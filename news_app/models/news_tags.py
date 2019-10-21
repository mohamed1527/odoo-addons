from odoo import fields, models


class NewsTags(models.Model):
    _name = 'news.tags'
    _description = 'tags information'
    tag_title = fields.Char('TagTitle', required=True)
    article_ids = fields.Many2many('news.article', string='Articles')