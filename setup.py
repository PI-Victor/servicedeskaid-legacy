try:
    import setuptools as s
except ImportError:
    import distutils.core as s


config = {
    'name': 'ServiceDeskAid',
    'include_package_data': True,
    'version': '0.1',
    'author': 'Victor Palade',
    'license': 'BSD',
    'url': 'http://github.com/codeflavour/servicedeskaid',
    'long_description': open('README.md').read(),
    'zip_safe': False,
    'packages': ['viewpanel'],
    'install_requires':[
        'flask',
        'flask-login',
        'flask-openid',
        'flask-script',
        'flask-wtf',
        'uwsgi',
        'sqlalchemy',
        'psycopg2',
    ],
}

s.setup(**config)
