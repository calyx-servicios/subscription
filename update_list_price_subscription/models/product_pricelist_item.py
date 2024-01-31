# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    @api.constrains("fixed_price")
    def _set_suscription_line_price(self):
        for product in self:
            variant_ids = product.mapped("product_tmpl_id.product_variant_ids").ids
            subscription_lines = self.env["sale.subscription.line"].search(
                [("product_id", "in", variant_ids)]
            )
            for line in subscription_lines:
                line.price_unit = product.fixed_price
