# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from cms.apphook_pool import apphook_pool
from cms.cms_menus import SoftRootCutter
from menus.menu_pool import menu_pool
from shop.cms_apphooks import CatalogListCMSApp, CatalogSearchCMSApp, OrderApp, PasswordResetApp


class CatalogListApp(CatalogListCMSApp):
    def get_urls(self, page=None, language=None, **kwargs):
        from shop.views.catalog import AddToCartView, ProductListView, ProductRetrieveView
        from giftshop.serializers import ProductDetailSerializer

        return [
            url(r'^$', ProductListView.as_view(
                redirect_to_lonely_product=True,
            )),
            url(r'^(?P<slug>[\w-]+)/?$', ProductRetrieveView.as_view(
                serializer_class=ProductDetailSerializer,
                lookup_field='translations__slug'
            )),
            url(r'^(?P<slug>[\w-]+)/add-to-cart', AddToCartView.as_view(lookup_field='translations__slug')),
        ]

apphook_pool.register(CatalogListApp)


class CatalogSearchApp(CatalogSearchCMSApp):
    def get_urls(self, page=None, language=None, **kwargs):
        from shop.search.views import SearchView
        from giftshop.serializers import ProductSearchSerializer

        return [
            url(r'^', SearchView.as_view(
                serializer_class=ProductSearchSerializer,
            )),
        ]

apphook_pool.register(CatalogSearchApp)

apphook_pool.register(OrderApp)

apphook_pool.register(PasswordResetApp)


def _deregister_menu_pool_modifier(Modifier):
    index = None
    for k, modifier_class in enumerate(menu_pool.modifiers):
        if issubclass(modifier_class, Modifier):
            index = k
    if index is not None:
        # intentionally only modifying the list
        menu_pool.modifiers.pop(index)

_deregister_menu_pool_modifier(SoftRootCutter)
