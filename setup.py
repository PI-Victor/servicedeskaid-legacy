try:
    import setuptools as s
except ImportError:
    import distutils.core as s

config = {
    'name': 'ServiceDeskAid',
    'include_package_data': True,
    'version': '0.1.0',
    'author': 'thecodeflavour.org',
    'url': 'http://codeflavour.github.io/servicedeskaid/',
    'long_description': open('README.md').read(),
    'zip_safe': False,
    'packages': s.find_packages(),
    'install_requires':[
        'flask',
        'flask-restful',
        'flask-mongoalchemy',
        'flask-login',
        'pygal',
    ],
}

s.setup(**config)
