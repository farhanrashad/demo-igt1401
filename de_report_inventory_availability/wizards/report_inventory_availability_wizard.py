from odoo import api, fields, models, _
from odoo.exceptions import UserError


class InventoryAvailabilityWizard(models.TransientModel):
    _name = "inventory.availability.wizard"
    _description = 'Inventory Availability Wizard'
    
    in_date =  fields.Datetime(string='Inventory Date')
    
    productids = fields.Many2many('product.product', 'report_inventory_availability_product_rel', 'report_inventory_availability_id',
        'product_id', 'Products')
    categ_ids = fields.Many2many('product.category', 'report_inventory_availability_categ_rel', 'report_inventory_availability_id',
        'categ_id', 'Categories')
    location_ids = fields.Many2many('stock.location', 'report_inventory_availability_location_rel', 'report_inventory_availability_id',
        'location_id', 'Locations')
    
    
    def print_report(self):
        #order_ids = self.env['stock.transfer.order'].browse(self._context.get('active_ids',[]))
        data = {
            'in_date': self.in_date, 
            'productids': self.productids.id,
            'categ_ids': self.categ_ids.id,
            'location_ids': self.location_ids.id,
        }
        if self.in_date:
            return self.env.ref('de_report_inventory_availability.report_inventory_availability_report').report_action(self, data=data)
