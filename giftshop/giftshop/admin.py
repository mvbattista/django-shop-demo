# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin
from cms.admin.placeholderadmin import PlaceholderAdminMixin, FrontendEditableAdminMixin
from shop.admin.defaults import customer
from shop.admin.defaults.order import OrderAdmin
from shop.models.defaults.order import Order
from shop.admin.order import PrintInvoiceAdminMixin
from shop.admin.delivery import DeliveryOrderAdminMixin
from shop.admin.defaults import commodity

admin.site.site_header = "giftshop Administration"


@admin.register(Order)
class OrderAdmin(PrintInvoiceAdminMixin, DeliveryOrderAdminMixin, OrderAdmin):
    pass


__all__ = ['commodity', 'customer']