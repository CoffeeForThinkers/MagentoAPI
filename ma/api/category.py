import logging

import ma.api.base_class

_LOGGER = logging.getLogger()


class CategoryApi(ma.api.base_class.Api):
    def info(self, category_id):
        arguments = { 'categoryId': category_id }
        i = self.magento.catalog_category.info(arguments)

        return i

    def assigned_products(self, category_id):
        arguments = { 'categoryId': category_id }
        i = self.magento.catalog_category.assignedProducts(arguments)
        return i

    def assign_product_by_id(self, category_id, product_id):
        r = self.magento.catalog_category.assignProduct(category_id, product_id)
        assert r == True, "Could not assign (by ID)"

    def assign_product_by_sku(self, category_id, product_sku):

        # NOTE(dustin): This is currently the same request as _id(), but we 
        #               want to keep the calls separate just in case Magento 
        #               gets their act together.
        r = self.magento.catalog_category.assignProduct(category_id, product_sku)
        assert r == True, "Could not assign (by SKU)"
