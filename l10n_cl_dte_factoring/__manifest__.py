# -*- coding: utf-8 -*-
{
    "name": """Cesión de Créditos Electrónica para Chile (factoring)\
    """,
    'version': '0.20.0',
    'category': 'Accounting',
    'sequence': 12,
    'author':  'Daniel Santibáñez Polanco',
    'website': 'https://globalresponse.cl',
    'license': 'AGPL-3',
    'summary': '',
    'description': """
Chile: Cesión de Documentos Tributarios.
""",
    'depends': [
        'l10n_cl_fe',
    ],
    'data': [
        'views/invoice_view.xml',
        #'views/partner_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
