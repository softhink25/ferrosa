# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    margen_minimo = fields.Float("Margen mínimo",related='company_id.margen_minimo', readonly=False)
