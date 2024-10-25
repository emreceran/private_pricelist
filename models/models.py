# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    pricelist_ids = fields.Many2many(
        'product.pricelist', string="Assigned Price Lists")


class Website(models.Model):
    _inherit = 'website'

    def get_pricelist_available(self, show_visible=False):
        """ Return the list of pricelists that can be used on website for the current user.
        Only the pricelists assigned to the user will be shown.
        Public users will see only the default website pricelist.
        """
        self.ensure_one()

        country_code = self._get_geoip_country_code()
        website = self.with_company(self.company_id)

        partner_sudo = website.env.user.partner_id
        is_user_public = self.env.user._is_public()

        if not is_user_public:
            # Kullanıcı özel fiyat listelerini alıyoruz
            last_order_pricelist = partner_sudo.last_website_so_id.pricelist_id
            partner_pricelist = partner_sudo.property_product_pricelist
            assigned_pricelists = partner_sudo.pricelist_ids

            # Eğer atanmış fiyat listesi yoksa genel fiyat listesini kullan
            if not assigned_pricelists:
                assigned_pricelists = website.sudo().pricelist_ids
        else:
            # Public kullanıcılar sadece varsayılan fiyat listesini görür
            last_order_pricelist = self.env['product.pricelist']
            partner_pricelist = website.sudo().pricelist_id  # Default website pricelist
            assigned_pricelists = partner_pricelist

        current_pricelist_id = self._get_cached_pricelist_id()

        pricelist_ids = website._get_pl_partner_order(
            country_code,
            show_visible,
            current_pl_id=current_pricelist_id,
            website_pricelist_ids=tuple(assigned_pricelists.ids),
            partner_pl_id=partner_pricelist.id,
            order_pl_id=last_order_pricelist.id)

        return self.env['product.pricelist'].browse(pricelist_ids)