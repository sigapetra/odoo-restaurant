from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    kitchen_station = fields.Selection(
        [
            ("none", "None"),
            ("kitchen", "Kitchen"),
            ("drink", "Drink"),
        ],
        string="Kitchen Station",
        default="none",
        help="Digunakan untuk routing tiket ke station yang tepat.",
    )


class PosKitchenOrder(models.Model):
    _name = "pos.kitchen.order"
    _description = "POS Kitchen Order"

    name = fields.Char(string="Reference", required=True, copy=False, default="New")
    session_id = fields.Many2one("pos.session", string="POS Session", required=True)
    order_id = fields.Many2one("pos.order", string="POS Order", required=True)
    station = fields.Selection(
        [("kitchen", "Kitchen"), ("drink", "Drink")],
        string="Station",
        required=True,
    )
    line_ids = fields.One2many(
        "pos.kitchen.order.line", "kitchen_order_id", string="Lines"
    )


class PosKitchenOrderLine(models.Model):
    _name = "pos.kitchen.order.line"
    _description = "POS Kitchen Order Line"

    kitchen_order_id = fields.Many2one(
        "pos.kitchen.order", string="Kitchen Order", required=True, ondelete="cascade"
    )
    product_id = fields.Many2one("product.product", string="Product", required=True)
    qty = fields.Float(string="Quantity", required=True)
    note = fields.Char(string="Note")
