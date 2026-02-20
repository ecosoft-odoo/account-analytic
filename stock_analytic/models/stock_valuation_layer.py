# Copyright 2026 Ecosoft Co., Ltd. (<http://ecosoft.co.th>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class StockValuationLayer(models.Model):
    _name = "stock.valuation.layer"
    _inherit = ["stock.valuation.layer", "analytic.mixin"]

    analytic_distribution = fields.Json(related="stock_move_id.analytic_distribution")
