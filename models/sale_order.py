# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp

import pytz
#from .tzlocal import get_localzone
#from odoo import tools
import logging
_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def getDomain(self):
        # if self:
        arr_products = self.env["product.product"].search([("id","=","26625")])
        # self.domain_productos = arr_products
        # return [('id', 'in', arr_products.mapped("id"))];
        return arr_products;
        # return [];

    domain_productos = fields.One2many('product.ptoduct', string='filtro', store=False, default=lambda self: self.getDomain())

    # domain = "[('sale_ok', '=', True), '|', ('company_id', '=', False), ('company_id', '=', parent.company_id)]"