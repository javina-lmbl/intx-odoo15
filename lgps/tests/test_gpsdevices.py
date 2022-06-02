from odoo.tests.common import TransactionCase


class TestGpsDevice(TransactionCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        user_admin = self.env.ref("base.user_admin")
        self.env = self.env(user=user_admin)
        self.GpsDevice = self.env["lgps.gpsdevice"]
        self.gpsdevice1 = self.GpsDevice.create({
            "name": "Testing Device",
            "status": "inventory",
            "product_id": 1,
            "client_id": 1,
            "serialnumber_id": 1,
            'active': True,

        })

    def test_gpsdevice_create(self):
        "New Devices are active by Default"
        self.assertEqual(
            self.gpsdevice1.active, True,
        )



