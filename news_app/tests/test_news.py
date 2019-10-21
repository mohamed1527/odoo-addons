from odoo.tests.common import TransactionCase


class TestNews(TransactionCase):

    def setUp(self,*args,**kwargs):

        result = super(TestNews,self).setUp(*args,**kwargs)
        group = self.env.ref('news_app.group_user',False)
        user_root = self.env.ref('base.user_root')
        self.env=self.env(user=user_root)
        group.write({'users':[(4,user_root.id)]})
        return result

    def test_article(self):

        record = self.env['news.article'].create({'title': 'Sports is Important'})
        self.assertEquals(record.title, 'Sports is Important')
        record.write({'title': 'Sports is not Important'})
        self.assertEquals(record.title, 'Sports is not Important')
        print(record.title)


    def test_tags(self):

        record = self.env['news.tags'].create({'tag_title': 'Match'})
        self.assertEquals(record.tag_title, 'Match')
        record.write({'tag_title': 'Match'})
        self.assertEquals(record.tag_title, 'Match')
        print(record.tag_title)


    def test_category(self):


         record = self.env['news.category'].create({'category_title': 'Sport'})
         self.assertEquals(record.category_title ,'Sport')
         record.write({'category_title':'Sport'})
         self.assertEquals(record.category_title, 'Sport')
         print(record.category_title)

    def test_author(self):


        record = self.env['res.partner'].create({'name': 'Mido'})
        self.assertEquals(record.name, 'Mido')
        record.write({'is_author':True})
        self.assertTrue(record.is_author)
        print(record.name)
