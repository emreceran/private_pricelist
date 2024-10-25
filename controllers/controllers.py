# -*- coding: utf-8 -*-
# from odoo import http
#
# from odoo import http
# from odoo.http import request
# from odoo.addons.website_sale.controllers.main import WebsiteSale
#
#
# class WebsiteSaleInherit(WebsiteSale):
#     @http.route(['/shop'], type='http', auth="public", website=True)
#     def shop(self, **kwargs):
#         # Mevcut kullanıcıyı alıyoruz
#         user = request.env.user
#
#         # Kullanıcıya atanmış fiyat listelerini alıyoruz
#         assigned_pricelists = request.env['product.pricelist'].search([('id', 'in', user.partner_id.pricelist_ids.ids)])
#
#         # Orijinal shop metodu çalıştırılıyor
#         response = super(WebsiteSaleInherit, self).shop(**kwargs)
#
#         # Pricelist verisini filtreliyoruz
#         response.qcontext['pricelists'] = assigned_pricelists
#         return response

# class PrivatePricelist(http.Controller):
#     @http.route('/private_pricelist/private_pricelist', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/private_pricelist/private_pricelist/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('private_pricelist.listing', {
#             'root': '/private_pricelist/private_pricelist',
#             'objects': http.request.env['private_pricelist.private_pricelist'].search([]),
#         })

#     @http.route('/private_pricelist/private_pricelist/objects/<model("private_pricelist.private_pricelist"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('private_pricelist.object', {
#             'object': obj
#         })
