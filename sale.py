# This file is part of the sale_shipment_comment module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Sale']


class Sale(metaclass=PoolMeta):
    __name__ = 'sale.sale'
    shipment_comment = fields.Text('Shipment Comment',
        states={
            'readonly': Eval('state') != 'draft',
            },
        depends=['state'])

    def _get_shipment_sale(self, Shipment, key):
        key += (('comment', self.shipment_comment),)
        return super(Sale, self)._get_shipment_sale(Shipment, key)
