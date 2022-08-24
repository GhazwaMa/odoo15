# -*- coding: utf-8 -*-
# Part of AppJetty. See LICENSE file for full copyright and licensing details.

{
    'name': 'Theme Scita',
    'summary': '''Mobile-first & most versatile Odoo theme. 
Perfect for E-Commerce, Fashion, IT, Furniture and other 35+ industries.''',
    'author': 'AppJetty',
    'website': 'https://www.appjetty.com/',
    'category': 'Theme/Ecommerce',
    'version': '14.0.1.0.2',
    'license': 'OPL-1',
    'description': '''Theme Scita
Business theme
Furniture theme
Hardware theme
Hardware and tools theme
Single Page theme
Digital security theme
Event theme
Medical equipments theme
multipurpose template for industry
multipurpose template for all industries
odoo custom theme
customizable odoo theme
multi industry odoo theme
multi purpose responsive odoo theme
multipurpose website template for odoo
odoo multipurpose theme for industry
multipurpose templates for odoo
odoo ecommerce templates
odoo ecommerce theme
odoo ecommerce themes
odoo responsive themes
odoo website themes
odoo ecommerce website theme
odoo theme for ecommerce store
odoo bootstrap themes
customize odoo theme
odoo ecommerce store theme for business
odoo theme for business
odoo responsive website theme
Scita Theme
Odoo Scita Theme
Scita theme for Odoo
odoo 11 theme
multipurpose theme
odoo multipurpose theme
odoo responsive theme
responsive theme
odoo theme
odoo themes
ecommerce theme
odoo ecommerce themes
odoo website themes
odoo bootstrap themes
bootstrap themes
bootstrap theme
customize odoo theme
ecommerce store theme
theme for business
theme for ecommerce store
Shop by category
publish unpublish product
AMP Support
    ''',
    'depends': [
        'sale_management',
        'website_sale',
        'website_sale_comparison',
        'website_sale_wishlist',
        'hr',
        'website_blog',
    ],
    'data': [
        'security/ir.model.access.csv',
        # 'views/assets.xml',
        'data/menu_data.xml',
        'data/theme_scita_data.xml',
        'data/extra_pages_data.xml',
        'data/scita_image_data.xml',
        'views/theme_cusomization.xml',
        'views/theme.xml',
        # 'views/cusomization_template.xml',
        'views/footer_option.xml',
        'views/header_option.xml',
        'views/res_config_view.xml',
        'views/views.xml',
        'views/res_company_view.xml',
        'data/data.xml',
        'views/sliders_view.xml',
        'views/website_view.xml',
        'views/brand_snippets.xml',
        'views/blogs_snippets.xml',
        'views/banner_snippets.xml',
        'views/case_study_snippets.xml',
        'views/service_snippets.xml',
        'views/testinomials_snippets.xml',
        'views/pricing_tables_snippets.xml',
        'views/our_team_snippets.xml',
        'views/policy_trust_snippets.xml',
        'views/newsletter_snippets.xml',
        'views/letstalk_snippets.xml',
        'views/how_it_work_snippets.xml',
        'views/expertise_statistics_snippets.xml',
        'views/contact_us_snippets.xml',
        'views/content_snippets.xml',
        'views/promo_banner_snippets.xml',
        'views/about_us_snippets.xml',
        'views/deal_of_day_snippets.xml',
        'views/client_snippets.xml',
        'views/category_snippets.xml',
        'views/timeline_snippets.xml',
        'views/protflio_snippets.xml',
        'views/snippet_google_map.xml',
        'views/snippets.xml',
        'views/product_details_template.xml',
        'views/shop_page_amp_template.xml',
        'views/shop_by_category.xml',
        'views/deal_of_day_page.xml',
        'views/pwa_config_view.xml',
        'views/pwa_template.xml',
    ],
    'support': 'support@appjetty.com',
    'live_test_url': 'http://theme-scita-v13.appjetty.com/',
    'images': [
        'static/description/splash-screen.png',
        'static/description/splash-screen_screenshot.gif',
    ],
    'application': True,
    'price': 198.00,
    'currency': 'EUR',
    'installable': True,
    'assets': {
        'web._assets_primary_variables': [
            ('before', 'website/static/src/scss/primary_variables.scss', '/theme_scita/static/src/scss/scita_fonts.scss'),
            '/theme_scita/static/src/scss/scita_primary_variables.scss'
        ],
        'web.assets_frontend': [
            '/theme_scita/static/src/css/owl.carousel.css',
            '/theme_scita/static/src/css/animate.css',
            '/theme_scita/static/src/css/ion.rangeSlider.css',
            '/theme_scita/static/src/css/ion.rangeSlider.skinHTML5.css',
            '/theme_scita/static/src/css/base.css',
            '/theme_scita/static/src/css/unite-gallery.css',
            '/theme_scita/static/src/fonts/line-icons.css',
            '/theme_scita/static/src/fonts/themify-icons.css',
            '/theme_scita/static/src/skins/alexis/alexis.css',

            '/theme_scita/static/src/scss/web.scss',
            '/theme_scita/static/src/scss/variable.scss',
            '/theme_scita/static/src/scss/mixins.scss',
            '/theme_scita/static/src/scss/comman.scss',
            '/theme_scita/static/src/scss/snippets.scss',
            '/theme_scita/static/src/scss/megamenu_style.scss',
            '/theme_scita/static/src/scss/product_style.scss',
            '/theme_scita/static/src/scss/checkout_style.scss',
            '/theme_scita/static/src/scss/demo/demo.scss',
            '/theme_scita/static/src/scss/cms_pages.scss',
            '/theme_scita/static/src/scss/header/default_header.scss',
            '/theme_scita/static/src/scss/footer/default_footer.scss',

            '/theme_scita/static/src/js/wow.min.js',
            '/theme_scita/static/src/js/owl.carousel.min.js',
            '/theme_scita/static/src/js/ion.rangeSlider.min.js',
            '/theme_scita/static/src/js/ug-theme-compact.js',
            '/theme_scita/static/src/js/unitegallery.min.js',
            '/theme_scita/static/src/js/scita_general.js',
            '/theme_scita/static/src/js/scita_fronted.js',
            '/theme_scita/static/src/js/timer_fronted.js',
            '/theme_scita/static/src/js/rating_state.js',
            '/theme_scita/static/src/js/product_details.js',
            '/theme_scita/static/src/js/see_more_brand.js',

            ### button_options

            ('after', '/theme_scita/static/src/scss/comman.scss',
             '/theme_scita/static/src/scss/button/button_style_1.scss'),
            ('after', '/theme_scita/static/src/scss/comman.scss',
             '/theme_scita/static/src/scss/button/button_style_2.scss'),
            ('after', '/theme_scita/static/src/scss/comman.scss',
             '/theme_scita/static/src/scss/button/button_style_3.scss'),
            ('after', '/theme_scita/static/src/scss/comman.scss',
             '/theme_scita/static/src/scss/button/button_style_4.scss'),
            ('after', '/theme_scita/static/src/scss/comman.scss',
             '/theme_scita/static/src/scss/button/button_style_5.scss'),
            ('after', '/theme_scita/static/src/scss/comman.scss',
             '/theme_scita/static/src/scss/button/button_style_6.scss'),
            ('after', '/theme_scita/static/src/scss/comman.scss',
             '/theme_scita/static/src/scss/button/button_style_7.scss'),
            ('after', '/theme_scita/static/src/scss/comman.scss',
             '/theme_scita/static/src/scss/button/button_style_8.scss'),


            ### footer
            '/theme_scita/static/src/scss/footer/footer_1.scss',
            '/theme_scita/static/src/scss/footer/footer_2.scss',
            '/theme_scita/static/src/scss/footer/footer_3.scss',
            '/theme_scita/static/src/scss/footer/footer_4.scss',
            '/theme_scita/static/src/scss/footer/footer_5.scss',
            '/theme_scita/static/src/scss/footer/footer_6.scss',
            '/theme_scita/static/src/scss/footer/footer_7.scss',
            '/theme_scita/static/src/scss/footer/footer_8.scss',
            '/theme_scita/static/src/scss/footer/footer_9.scss',
            '/theme_scita/static/src/scss/footer/footer_10.scss',
            '/theme_scita/static/src/scss/footer/footer_11.scss',
            '/theme_scita/static/src/scss/footer/footer_12.scss',
            '/theme_scita/static/src/scss/footer/footer_13.scss',
            '/theme_scita/static/src/scss/footer/footer_14.scss',
            '/theme_scita/static/src/scss/footer/footer_15.scss',
            '/theme_scita/static/src/scss/footer/footer_16.scss',
            '/theme_scita/static/src/scss/footer/footer_17.scss',
            '/theme_scita/static/src/scss/footer/footer_18.scss',
            '/theme_scita/static/src/scss/footer/footer_19.scss',
            '/theme_scita/static/src/scss/footer/footer_20.scss',
            '/theme_scita/static/src/scss/footer/footer_21.scss',
            '/theme_scita/static/src/scss/footer/footer_22.scss',
            '/theme_scita/static/src/scss/footer/footer_23.scss',
            '/theme_scita/static/src/scss/footer/footer_24.scss',
            '/theme_scita/static/src/scss/footer/footer_25.scss',
            '/theme_scita/static/src/scss/footer/footer_26.scss',

            ### headers

            '/theme_scita/static/src/scss/header/header_1.scss',
            '/theme_scita/static/src/js/header.js',

            '/theme_scita/static/src/scss/header/header_2.scss',

            '/theme_scita/static/src/scss/header/header_3.scss',

            '/theme_scita/static/src/scss/header/header_4.scss',

            '/theme_scita/static/src/scss/header/header_5.scss',

            '/theme_scita/static/src/scss/header/header_service_1.scss',

            '/theme_scita/static/src/scss/header/header_service_1.scss',

            '/theme_scita/static/src/scss/header/header_service_2.scss',

            '/theme_scita/static/src/scss/header/header_6.scss',

            '/theme_scita/static/src/js/wishlist_products.js',

            '/theme_scita/static/src/scss/header/header_7.scss',

            '/theme_scita/static/src/scss/header/header_8.scss',

            '/theme_scita/static/src/scss/header/header_9.scss',

            '/theme_scita/static/src/scss/header/header_10.scss',

            '/theme_scita/static/src/scss/header/header_11.scss',

            '/theme_scita/static/src/scss/header/header_12.scss',

            '/theme_scita/static/src/scss/header/header_13.scss',

            '/theme_scita/static/src/scss/header/header_14.scss',

            '/theme_scita/static/src/scss/header/header_15.scss',

            '/theme_scita/static/src/scss/header/header_16.scss',

            '/theme_scita/static/src/scss/header/header_17.scss',

            '/theme_scita/static/src/scss/header/header_18.scss',

            '/theme_scita/static/src/scss/header/header_19.scss',

            '/theme_scita/static/src/scss/header/header_20.scss',

        ],
        'web.assets_editor': [
            '/theme_scita/static/src/js/scita_editor.js',
            '/theme_scita/static/src/js/timer_editor.js',
            '/theme_scita/static/src/js/google_map_editor.js'
        ]

    }

}
