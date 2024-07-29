# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom Ultravaiolet commands"""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'pytest-invenio>=1.4.0',
    'psycopg2>=2.9.5',
]

extras_require = {
    'docs': [
        'Sphinx>=3,<4',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

setup_requires = [
    'Babel>=2.8',
]

# install_requires = [
#     'click>=8.1.3',
#     'Flask>=2.2.2',
#     'Flask-BabelEx>=0.9.4',
#     'invenio-i18n>=1.2.0',
#     'invenio-files-rest>=1.4.0',
#     'invenio-access>=1.4.4',
#     'invenio-accounts>=2.0.0',
#     'invenio-app>=1.3.4',
#     'invenio-pidstore>=1.2.3',
#     'invenio-rdm-records>=1.0.0',
#     'invenio-search>=2.1.0',
#     'opensearch-dsl>=2.0.0',
#     'opensearch-py>=2.0.0',
#     'jsonschema>=4.17.3',
#     'requests>=2.28.2',
#     # 'Sphinx>=3,<4',
#     'sphinx>=5.2.1',
#     'Werkzeug==2.2.2',
# ]

install_requires = [
    'alembic==1.11.1',
    'amqp==5.1.1',
    'arrow==1.2.3',
    'asttokens==2.2.1',
    'async-timeout==4.0.2',
    'attrs==23.1.0',
    'babel==2.10.3',
    'babel-edtf==1.0.0',
    'billiard==3.6.4.0',
    'bleach==6.0.0',
    'blinker==1.6.2',
    'celery==5.2.7',
    'certifi==2023.5.7',
    'cffi==1.15.1',
    'charset-normalizer==3.1.0',
    'click==8.1.3',
    'click-default-group==1.2.2',
    'click-didyoumean==0.3.0',
    'click-repl==0.2.0',
    'cryptography==41.0.1',
    'datacite==1.1.3',
    'dnspython==2.3.0',
    'dojson==1.4.0',
    'email-validator==2.0.0.post2',
    'executing==1.2.0',
    'faker==18.10.1',
    'Flask>=2.2.2',
    'Flask-BabelEx>=0.9.4',
    'flask-caching==2.0.2',
    'flask-cors==3.0.10',
    'flask-iiif==0.6.3',
    'flask-limiter==1.1.0',
    'flask-login==0.6.2',
    'flask-menu==0.7.2',
    'flask-resources==0.9.1',
    'flask-security-invenio==3.1.4',
    'flask-wtf==1.1.1',
    'future==0.18.3',
    'geojson==3.0.1',
    'github3.py==4.0.1',
    'idna==3.4',
    'importlib-metadata==4.13.0',
    'importlib-resources==5.12.0',
    'invenio-admin==1.3.2',
    'invenio-administration==1.0.6',
    'invenio-app>=1.3.4',
    'invenio-assets==2.0.0',
    'invenio-base==1.2.15',
    'invenio-cache==1.1.1',
    'invenio-celery==1.2.5',
    'invenio-i18n>=1.2.0',
    'invenio-files-rest>=1.4.0',
    'invenio-access>=1.4.4',
    'invenio-accounts>=2.0.0',
    'invenio-pidstore>=1.2.3',
    'invenio-rdm-records>=1.0.0',
    'invenio-search>=2.1.0',
    'invenio-communities==4.1.1',
    'jedi==0.18.2',
    'jinja2==3.1.2',
    'jsonpatch==1.32',
    'jsonpointer==2.3',
    'jsonschema>=4.17.3',
    'kombu==5.3.0',
    'limits==1.6',
    'lxml==4.9.2',
    'mako==1.2.4',
    'markupsafe==2.1.3',
    'marshmallow==3.19.0',
    'marshmallow-oneofschema==3.0.1',
    'matplotlib-inline==0.1.6',
    'maxminddb==2.3.0',
    'mistune==0.8.4',
    'msgpack==1.0.5',
    'opensearch-dsl>=2.0.0',
    'opensearch-py>=2.0.0',
    'packaging==23.1',
    'parso==0.8.3',
    'pexpect==4.8.0',
    'pillow==9.5.0',
    'prompt-toolkit==3.0.38',
    'psycopg2-binary==2.9.6',
    'pure-eval==0.2.2',
    'pycountry==22.3.5',
    'pycparser==2.21',
    'pygments==2.15.1',
    'pyjwt==2.7.0',
    'pymysql==1.1.0rc1',
    'pynpm==0.1.2',
    'pyparsing==3.1.0b2',
    'python-dateutil==2.8.2',
    'pytz==2023.3',
    'pywebpack==1.2.0',
    'pyyaml==6.0',
    'redis==5.0.0b4',
    'referencing==0.29.0',
    'requests>=2.28.2',
    # 'sphinx>=5.2.1',
    'Sphinx>=3,<4',
    'rpds-py==0.7.1',
    'sentry-sdk==1.25.1',
    'setuptools==67.8.0',
    'simplejson==3.19.1',
    'sqlalchemy==1.4.48',
    'sqlalchemy-continuum==1.3.15',
    'stack-data==0.6.2',
    'traitlets==5.9.0',
    'typing-extensions==4.6.3',
    'ua-parser==0.16.1',
    'uritools==4.0.1',
    'urllib3==1.26.16',
    'validators==0.20.0',
    'vine==5.0.0',
    'wand==0.6.11',
    'wcwidth==0.2.6',
    'Werkzeug==2.2.2',
    'zipp==3.15.0',
    'zipstream-ng==1.6.0',
    'python-dotenv',
    'invenio-app-rdm',
]


packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('ultraviolet_cli', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='ultraviolet-cli',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='invenio TODO',
    license='MIT',
    author='NYU Libraries',
    author_email='nyu-data-repository@nyu.edu',
    url='https://github.com/nyudlts/ultraviolet-cli',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'ultraviolet-cli=ultraviolet_cli.cli:cli',
            'uv-cli=ultraviolet_cli.cli:cli' # alias shorthand
        ]
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.9',
        'Development Status :: 1 - Planning',
    ],
)
