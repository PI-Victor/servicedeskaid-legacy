try:
    import setuptools as s
except ImportError:
    import distutils.core as s

import sys

config = {
    'name' : 'ServiceDeskAid',
    'include_package_data' : True,
    'zip_safe' : False,
    'packages' : s.find_packages(),
    'install_requires': [
        'mysql-connector-python',
        'sqlalchemy',
        'flask',
        'flask-restful'
    ],
}

s.setup(**config)
