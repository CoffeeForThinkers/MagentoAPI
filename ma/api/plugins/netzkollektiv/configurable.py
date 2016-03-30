import logging
import collections

import ma.api.base_class
import ma.entities.product
import ma.utility

_LOGGER = logging.getLogger(__name__)


class ConfigurableApi(ma.api.base_class.Api):
    def assign_simple_product_to_configurable_product(
            self, configurable_product_id, simple_sku_list, attribute_codes, 
            attribute_labels, pricing_list):
        """`attribute_codes`: A list of attribute codes to group configuration on.
        
        `attributes_labels`: A dictionary of labels for the attribute codes.
        
        `pricing` is a dictionary keyed by all of the values for all of the 
        attributes that we're grouping by. Yes, there will be collisions if any 
        observed values between any of the grouped attributes happen to match.
        """

        _LOGGER.debug("Assigning simple products to configurable with ID "
                      "(%d): %s", configurable_product_id, simple_sku_list)

        arguments = [
            configurable_product_id,
            simple_sku_list,
            attribute_codes,
            attribute_labels,
            pricing_list,
        ]

        (c, sid) = self.soap2
        c.catalogProductTypeConfigurableAssign(*([sid] + arguments))
