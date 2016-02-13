#!/usr/bin/env python2.7

import datetime

import ma.api.catalog_category
import ma.api.catalog_product
import ma.api.core_store
import ma.api.magento_info
import ma.api.sales_order_invoice
import ma.api.catalog_product_attribute_set
import ma.api.catalog_product_attribute
import ma.api.catalog_product_attribute_media
import ma.api.catalog_product_tag
import ma.api.cataloginventory_stock_item
import ma.api.catalog_product_type
import ma.utility

def _sales_order_invoice():
    soi = ma.api.sales_order_invoice.SalesOrderInvoiceApi()

    start = datetime.datetime(year=2013, month=05, day=29, hour=0, minute=0, second=0)
    stop = start + datetime.timedelta(seconds=86400)

    return soi.get_transactions(start, stop)

def _catalog_category():
    cc = ma.api.catalog_category.CatalogCategoryApi()
#    r = c.info(1)

    return cc.get_tree()

#    product_id = 295
    product_sku = 'wbk013'
    category_id = 1

#    c.assign_product_with_id(category_id, product_id)
    cc.assign_product_with_id(category_id, product_sku)

#    r = c.assigned_products(1)
#    r = c.assigned_products(10)
    r = cc.get_tree(10)
    
    return r
    
def _catalog_product():
    cp = ma.api.catalog_product.CatalogProductApi()
#    r = p.get_info_with_id(314)
#    r = p.info_with_sku('wsd017')
    r = cp.get_list()#([19])

    return r

def _core_store():
    cs = ma.api.core_store.CoreStoreApi()
    l = cs.get_list()

    return l

def _magento():
    m = ma.api.magento_info.MagentoInfoApi()
    l = m.get_info()

    return l

def _catalog_product_attribute_set():
    cpas = ma.api.catalog_product_attribute_set.CatalogProductAttributeSetApi()
    l = cpas.get_list()
    l = list(l)

    return l

def _catalog_product_attribute():
    cpa = ma.api.catalog_product_attribute.CatalogProductAttributeApi()
    l = cpa.get_list(18)

    return l

def _catalog_product_attribute_media():
    cpam = ma.api.catalog_product_attribute_media.CatalogProductAttributeMediaApi()
    l = cpam.get_list_with_product_id(234)

    return l

def _catalog_product_tag():
    cpt = ma.api.catalog_product_tag.CatalogProductTagApi()
    l = cpt.get_list(405)

    return l

def _cataloginventory_stock_item():
    csi = ma.api.cataloginventory_stock_item.CatalogInventoryStockItemApi()
#    l = csi.get_list_with_ids([405, 231, 232, 999])
    l = csi.get_list_with_ids([405, 231, 232])

    return l

def _catalog_product_type():
    cpt = ma.api.catalog_product_type.CatalogProductTypeApi()
    l = cpt.get_list()

    return l

if __name__ == '__main__':
    r = _catalog_category()
#    r = _catalog_product()
#    r = _store()
#    r = _magento()
#    r = _sales()
#    r = _catalog_product_attribute_set()
#    r = _catalog_product_attribute()
#    r = _catalog_product_attribute_media()
#    r = _catalog_product_tag()
#    r = _cataloginventory_stock_item()
#    r = _catalog_product_type()

    ma.utility.pretty_print(r)
