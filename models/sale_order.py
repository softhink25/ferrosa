# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp

import pytz
#from .tzlocal import get_localzone
#from odoo import tools
import logging
from odoo.exceptions import AccessError, UserError, ValidationError

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for order in self:
            porcentaje = (order.company_id.margen_minimo/100)
            for linea in order.order_line:
                costo = linea.product_id.standard_price + (linea.product_id.standard_price * (porcentaje));
                if linea.price_unit < costo:
                    raise ValidationError(_(
                        "Actualice el precio de venta del producto %(producto)s, no cumple con el margen necesario.",
                        producto=linea.product_id.display_name,
                    ))
            return super(SaleOrder, order).action_confirm()


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'


    modifica_precio = fields.Boolean("Modifica precio", compute ="_usuario_modifica_precio")

    def _usuario_modifica_precio(self):
        for linea in self:
            linea.modifica_precio = self.env.user.cambia_precio

    def getDomain(self):
        if self:
            arr_products = self.env["product.product"].search([], limit=5)
            self.domain_productos = arr_products.mapped("id")
            # return [('id', 'in', arr_products.mapped("id"))];
            return arr_products;
        return [];

    # @api.model
    # def default_get(self, fields_list):
    #     res = super(SaleOrderLine, self).default_get(fields_list)
    #     arr_products = self.env["product.product"].search([], limit=5)
    #     # arr_lines = [(5,0,0)];
    #     arr_lines = [];
    #     for product in arr_products:
    #         arr_lines.append(product.id)
    #         # arr_lines.append((0,0,{
    #         #     "product_id" : product.id
    #         # }))
    #     # vals = [(0, 0, {'domain_productos': arr_products.ids})]
    #     res.update({'domain_productos': arr_lines})
    #     return res

    def getDefault(self):
        # if self:
        return  self.env["product.product"].search([], limit=5)
        # self.domain_productos = arr_products.mapped("id")
        # return arr_products.ids
        # return arr_products;
        # return [];

    #  default=lambda self: self.getDefault()
    # ,compute=getDomain,
    domain_productos = fields.One2many('product.ptoduct', string='filtro', store=False)

    # domain = "[('sale_ok', '=', True), '|', ('company_id', '=', False), ('company_id', '=', parent.company_id)]"