#!/usr/bin/env python2.7

import bma.api.category
import bma.utility

def _main():
    c = bma.api.category.CategoryApi()
#    r = c.info(1)

#    product_id = 295
    product_sku = 'wbk013'
    category_id = 1

#    c.assign_product_by_id(category_id, product_id)
    c.assign_product_by_id(category_id, product_sku)

    r = c.assigned_products(1)
#    r = c.assigned_products(10)
    bma.utility.pretty_print(r)
    

if __name__ == '__main__':
    _main()
