import logging

import ma.api.base_class

_LOGGER = logging.getLogger()


class CatalogCategoryApi(ma.api.base_class.Api):
    def get_info(self, category_id):
        i = self.magento.catalog_category.info(category_id)

        return i

    def assigned_products(self, category_id):
        i = self.magento.catalog_category.assignedProducts(category_id)
        return i

    def assign_product_with_id(self, category_id, product_id):
        r = self.magento.catalog_category.assignProduct(category_id, product_id)
        assert r == True, "Could not assign (by ID)"

    def assign_product_with_sku(self, category_id, product_sku):

# NOTE(dustin): This is currently the same request as _id(), but we want to
#               keep the calls separate just in case Magento finally gets their 
#               act together.
        r = self.magento.catalog_category.assignProduct(category_id, product_sku)
        assert r == True, "Could not assign (by SKU)"

    def get_tree(self, parent_id=None):
        args = []
        kwargs = {}
        if parent_id is not None:
            kwargs['parentCategory'] = parent_id

        t = self.magento.catalog_category.level(*args, **kwargs)
        return t
