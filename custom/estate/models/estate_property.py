from odoo import models, fields, api

class EstatePropertyModel(models.Model):
    _name = 'estate.property'
    _description = 'Estate property'

    name = fields.Char('Title', required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availibility = fields.Date('Available From', copy=False,default=lambda self: fields.Datetime.today())
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer('Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()    
    garden_orientation = fields.Selection([
        ('North', 'North'),
        ('South', 'South'),
        ('East', 'East'),
        ('West','West'),
    ])
    state = fields.Selection([
        ('New', 'New'),
        ('Offer Received', 'Offer Received'),
    ])
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    user_id = fields.Many2one('res.users', string='Salesperson', index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.users', string='Buyer', index=True)
    tag_ids = fields.Many2many('estate.property.tag', string='Property Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')
    # total_area = fields.Float(compute='_compute_total_area')

    # @api.depends('living_area', 'garden_area')
    # def _compute_total_area(self):
    #     for record in self:
    #         record.total_area = 2.0 * record.living_area