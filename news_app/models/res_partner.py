from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    is_author = fields.Boolean("Is Author ? ")
    article_ids = fields.Many2many('news.article', string='Articles')