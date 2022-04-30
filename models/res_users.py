# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp

import pytz
#from .tzlocal import get_localzone
#from odoo import tools
import logging
from odoo.exceptions import AccessError, UserError, ValidationError

_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = 'res.users'

    cambia_precio = fields.Boolean("Puede cambiar precio")
