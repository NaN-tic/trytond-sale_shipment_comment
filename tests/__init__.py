# This file is part of the sale_shipment_comment module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
try:
    from trytond.modules.sale_shipment_comment.tests.test_sale_shipment_comment import suite
except ImportError:
    from .test_sale_shipment_comment import suite

__all__ = ['suite']
