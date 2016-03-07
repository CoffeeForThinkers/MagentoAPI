import logging
import collections

import ma.api.base_class
import ma.entities.product
import ma.utility

_LOGGER = logging.getLogger()


class CatalogProductTypeConfigurableApi(ma.api.base_class.Api):
    def __assign(self, configurable_id_or_sku, simple_id_or_sku_list, 
                 group_by_attributes_list, group_labels, 
                 configurable_attributes):
        """Given a configuration product, assign a list of simple products to 
        it. This depends on an extension. See 
        http://netzkollektiv.com/blog/add-configurable-products-via-soapxml-rpc
        for the only documentation in existence.

        configurable_id_or_sku
            Configurable product

        simple_id_or_sku_list
            List of simple products

        group_by_attributes_list
            Names of attributes to group by

        group_labels
            Labels for the attributes being grouped-by.
        
        configurable_attributes
            A dictionary of dictionaries providing additional information 
            required for each group. This is a single dictionary that combines 
            such information for all potential values of the categories that 
            we're grouping by (e.g. if we're group by color and size, the keys 
            are a combination of all possible colors and sizes and the values 
            are dictionaries describing pricing information).
        """

        assert \
            issubclass(simple_id_or_sku_list.__class__, list), \
            "Simple products must be a list."

        assert \
            issubclass(group_by_attributes_list.__class__, list), \
            "Group-by attributes must be a list."

        assert \
            issubclass(group_labels.__class__, dict), \
            "Group labels must be a dictionary."

        assert \
            issubclass(configurable_attributes.__class__, dict), \
            "Group configurations must be a dictionary or dictionaries."

        id_ = \
            self.magento.catalog_product_type_configurable.assign(
                configurable_id_or_sku, 
                simple_id_or_sku_list, 
                group_by_attributes_list, 
                group_labels, 
                configurable_attributes
            )

        return id_

    def assign_with_main_id_and_sub_id_list(self, *args):

# NOTE(dustin): Both ID and SKU have the same calls, but we want to separate 
#               them just in case Magento finally gets their act together.
        id_ = self.__assign(*args)
        return id_

    def assign_with_main_sku_and_sub_sku_list(self, *args):

# NOTE(dustin): Both ID and SKU have the same calls, but we want to separate 
#               them just in case Magento finally gets their act together.
        id_ = self.__assign(*args)
        return id_
