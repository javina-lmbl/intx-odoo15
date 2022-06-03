from odoo import api, models, fields, _


class Partner(models.Model):
    _inherit = 'res.partner'

    gpsdevice_ids = fields.One2many(
        comodel_name="lgps.gpsdevice",
        inverse_name="client_id",
        string=_("Gps Devices"),
        readonly=True,
    )

    first_installation_day = fields.Date(
        string=_("First Installation Day")
    )

    credit_and_collection = fields.Many2one(
        comodel_name="res.users",
        string=_("Credit and collection"),
        ondelete="set null",
        index=True,
        domain=[('active', '=', True)],
        tracking=True,
    )

    after_sales = fields.Many2one(
        comodel_name="res.users",
        string=_("After Sales"),
        ondelete="set null",
        index=True,
        domain=[('active', '=', True)],
        tracking=True,
    )

    coordinator = fields.Many2one(
        comodel_name="res.users",
        string=_("Coordination"),
        ondelete="set null",
        index=True,
        domain=[('active', '=', True)],
        tracking=True,
    )

    client_type = fields.Selection(
        [
            ('new', _('New')),
            ('aftersales', _('After Sales')),
        ],
        default='new',
        string=_("Client Type")
    )

    client_status = fields.Selection(
        [
            ('active', _('Active')),
            ('draft', _('Draft')),
            ('cancelled', _('Cancelled')),
            ('demo', _('Demo')),
            ('inactive', _('Inactive')),
            ('suspended', _('Suspended')),
            ('negotiation', _('Negotiation')),
            ('negotiation', _('Negotiation')),
            ('irrecoverable', _('Irrecoverable')),
            ('financially_charged', _('Financially Charged')),
        ],
        default='draft',
        string=_("Client Status")
    )

    client_rating = fields.Selection(
        [
            ('a', _('A')),
            ('b', _('B')),
            ('c', _('C')),
            ('d', _('D')),
        ],
        default='d',
        string=_("Client rating")
    )

    custom_negotiations = fields.Boolean(
        default=False,
        string=_("Custom Negotiations"),
        tracking=True
    )
