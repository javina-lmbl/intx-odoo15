from odoo import api, models, fields, _


class Ticket(models.Model):
    _inherit = 'helpdesk.ticket'

    gpsdevice_id = fields.Many2one(
        comodel_name="lgps.gpsdevice",
        string=_("Gps Device"),
        ondelete="set null",
        index=True,
    )

    accessory_id = fields.Many2one(
        comodel_name="lgps.accessory",
        string=_("Accessory"),
        ondelete="set null",
        index=True,
    )

    closed_date = fields.Date(
        string=_("Closed Date"),
    )

    days_count = fields.Integer(
        compute='_compute_days_count',
        store=True,
        string=_("Open Days"),
    )

    ticket_id = fields.Many2one(
        comodel_name="helpdesk.ticket",
        string=_("Related Ticket"),
        ondelete="set null"
    )

    @api.depends('closed_date')
    def _compute_days_count(self):
        for record in self:
            if record.closed_date and record.create_date:
                start_dt = fields.Date.from_string(record.create_date)
                end_today_dt = fields.Date.from_string(record.closed_date)
                difference = end_today_dt - start_dt
                time_difference_in_days = difference.days
                record.days_count = time_difference_in_days
