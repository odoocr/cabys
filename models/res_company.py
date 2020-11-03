# -*- coding: utf-8 -*-

import logging, re
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


_logger = logging.getLogger(__name__)


class ResCompany(models.Model):

    _inherit = 'res.company'

    cabys_product_id = fields.Many2one("cabys.producto", "Código Cabys para productos sin codigo asignado")
