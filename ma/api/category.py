import logging

import ma.api.base_class

_LOGGER = logging.getLogger(__name__)


class CategoryApi(ma.api.base_class.Api):
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

    def create(self, parent_id, category_data):
        i = self.magento.catalog_category.create(parent_id, category_data)
        return i

    def update(self, category_id, category_data):
        is_updated = self.magento.catalog_category.update(category_id, category_data)
        return is_updated

    def delete(self, category_id):
        is_deleted = self.magento.catalog_category.delete(category_id)
        return is_deleted

    def update_active_status(self, category_id, is_active=True):
        # magento requires sorting values to be passed
        is_updated = self.magento.catalog_category.update(
            category_id,
            { 'is_active': str(int(is_active)),
              'available_sort_by': 'position',
              'default_sort_by': 'position' })
        return is_updated

    def get_tree(self, parent_id=1):
        t = self.magento.catalog_category.tree()
        return t
