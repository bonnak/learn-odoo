from typing import Tuple
from odoo import models, fields

class EstatePropertyOfferModel(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate property offer'

    price = fields.Float()
    status = fields.Selection([
        ('Accepted', 'Accepted'),
        ('Refused', 'Refused'),
    ], copy=False)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)