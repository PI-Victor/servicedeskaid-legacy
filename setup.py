try:
    import setuptools as s
except ImportError:
    import distutils.core as s


config = {
    'name': 'ServiceDeskAid',
    'include_package_data': True,
    'version': 'unversioned',
    'author': 'thecodeflavour.org',
    'url': 'http://github.com/codeflavour/servicedeskaid',
    'long_description': open('README.md').read(),
    'zip_safe': False,
    'packages': s.find_packages(),
    'install_requires':[
        'flask',
        'flask-mongoengine',
        'flask-login',
        'flask-openid',
        'flask-script',
        'flask-wtf',
        'jinja2',
        'pygal',
        'pillow',
        'uwsgi',
    ],
}

s.setup(**config)
