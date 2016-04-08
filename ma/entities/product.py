import collections

CATALOG_PRODUCT_CREATE_ENTITY = \
    collections.namedtuple(
        'CATALOG_PRODUCT_CREATE_ENTITY', [
            'categories',
            'websites',
            'name',
            'description',
            'short_description',
            'weight',
            'status',
            'url_key',
            'url_path',
            'visibility',
            'category_ids',
            'website_ids',
            'has_options',
            'gift_message_available',
            'price',
            'special_price',
            'special_from_date',
            'special_to_date',
            'tax_class_id',
            'tier_price',
            'meta_title',
            'meta_keyword',
            'meta_description',
            'custom_design',
            'custom_layout_update',
            'options_container',
            'stock_data',
        ])

def build_catalog_product_create_entity(*args, **kwargs):

    t = CATALOG_PRODUCT_CREATE_ENTITY(*args, **kwargs)

    # Add any validation here.

    return t

CATALOG_PRODUCT_TIER_PRICE_ENTITY = \
    collections.namedtuple(
        'CATALOG_PRODUCT_TIER_PRICE_ENTITY', [
            'customer_group_id',
            'website',
            'qty',
            'price',
        ])

def build_catalog_product_tier_price_entity(*args, **kwargs):

    t = CATALOG_PRODUCT_TIER_PRICE_ENTITY(*args, **kwargs)

    # Add any validation here.

    return t

CATALOG_INVENTORY_STOCK_ITEM_UPDATE_ENTITY = \
    collections.namedtuple(
        'CATALOG_INVENTORY_STOCK_ITEM_UPDATE_ENTITY', [
            'qty',
            'is_in_stock',
            'manage_stock',
            'use_config_manage_stock',
            'min_qty',
            'use_config_min_qty',
            'min_sale_qty',
            'use_config_min_sale_qty',
            'max_sale_qty',
            'use_config_max_sale_qty',
            'is_qty_decimal',
            'backorders',
            'use_config_backorders',
            'notify_stock_qty',
            'use_config_notify_stock_qty',
        ])

def build_catalog_inventory_stock_item_update_entity(*args, **kwargs):

    t = CATALOG_INVENTORY_STOCK_ITEM_UPDATE_ENTITY(*args, **kwargs)

    # Add any validation here.

    return t

CATALOG_PRODUCT_IMAGE_FILE_ENTITY = \
    collections.namedtuple(
        'CATALOG_PRODUCT_IMAGE_FILE_ENTITY', [
            'content',
            'mime',
            'name',
        ])

def build_catalog_product_image_file_entity(*args, **kwargs):

    t = CATALOG_PRODUCT_IMAGE_FILE_ENTITY(*args, **kwargs)

    # Add any validation here.

    return t


CATALOG_PRODUCT_ATTRIBUTE_MEDIA_CREATE_ENTITY = \
    collections.namedtuple(
        'CATALOG_PRODUCT_ATTRIBUTE_MEDIA_CREATE_ENTITY', [
            'file',
            'label',
            'position',
            'types',
            'exclude',
            'remove',
        ])

def build_catalog_product_attribute_media_create_entity(*args, **kwargs):

    t = CATALOG_PRODUCT_ATTRIBUTE_MEDIA_CREATE_ENTITY(*args, **kwargs)

    # Add any validation here.

    return t

CATALOG_PRODUCT_ENTITY = \
    collections.namedtuple(
        'CATALOG_PRODUCT_ENTITY', [
            'product_id',
            'sku',
            'name',
            'set',
            'type',
            'category_ids',
            'website_ids',
        ])

def build_catalog_product_entity(*args, **kwargs):

    t = CATALOG_PRODUCT_ENTITY(*args, **kwargs)

    # Add any validation here.

    return t
