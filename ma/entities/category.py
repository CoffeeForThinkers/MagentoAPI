import collections


CATALOG_CATEGORY_CREATE_ENTITY = \
    collections.namedtuple(
        'CATALOG_CATEGORY_CREATE_ENTITY', [
            'name',
            'is_active',
            'position',
            'available_sort_by',
            'custom_design',
            'custom_apply_to_products',
            'custom_design_from',
            'custom_design_to',
            'custom_layout_update',
            'default_sort_by',
            'description',
            'display_mode',
            'is_anchor',
            'landing_page',
            'meta_description',
            'meta_keywords',
            'meta_title',
            'page_layout',
            'url_key',
            'include_in_menu',
            'filter_price_range',
            'custom_use_parent_settings',
        ])

def build_catalog_category_create_entity(*args, **kwargs):

    t = CATALOG_CATEGORY_CREATE_ENTITY(*args, **kwargs)

    # Add any validation here.

    return t
