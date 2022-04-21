# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp

import pytz
#from .tzlocal import get_localzone
#from odoo import tools
import logging
from odoo.exceptions import AccessError, UserError, ValidationError

_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    precio_minimo = fields.Float("Precio mínimo", compute="_precio_minimo")

    def _precio_minimo(self):
        for producto in self:
            costo = producto.standard_price + (producto.standard_price * (.05));
            producto.precio_minimo = costo;
