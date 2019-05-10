# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from shop.models.defaults.commodity import Commodity
from django.db import models
from django.utils.translation import ugettext_lazy as _
from shop.models.defaults.cart import Cart
from shop.models.defaults.cart_item import CartItem
from shop.models.order import BaseOrderItem
from shop.models.defaults.delivery import Delivery
from shop.models.defaults.delivery_item import DeliveryItem
from shop.models.defaults.order import Order
from shop.models.defaults.mapping import ProductPage, ProductImage
from shop.models.defaults.address import BillingAddress, ShippingAddress
from shop.models.defaults.customer import Customer


__all__ = ['Cart', 'CartItem', 'Order', 'Delivery', 'DeliveryItem', 'BillingAddress', 'ShippingAddress', 'Customer', 'Commodity',]

class OrderItem(BaseOrderItem):
    quantity = models.IntegerField(_("Ordered quantity"))
    canceled = models.BooleanField(_("Item canceled "), default=False)
