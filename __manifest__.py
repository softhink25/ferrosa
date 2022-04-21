# coding: utf-8

{
    'name': 'Ferrosa',
    'version': '11.0.1.0.0',
    'author': 'Softhink',
    'maintainer': 'Softhink',
    'website': 'http://www.sft.com.mx',
    'license': 'AGPL-3',
    'category': 'Point of sale',
    'summary': 'Pago de servicios',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'ferrosa/static/src/js/**/*',
        ],
        'web.assets_qweb': [
            'ferrosa/static/src/xml/**/*',
        ],
    },
    # 'qweb': [
    #     'static/src/xml/pos.xml',
    # ],
    'data': [
        'views/external_template_view.xml',
        'report/stock_report_delivery.xml',

        # 'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': True,
    'demo': [],
    'test': []
}
