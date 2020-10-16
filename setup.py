# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as f:
    __doc__ = f.read()

setup(
    name='browsepy',
    license='MIT',
    long_description=__doc__,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    keywords = ['web', 'file', 'browser'],
    packages=[
        'browsepy',
        'browsepy.plugin',
        'browsepy.plugin.player',
        ],
    package_data={ # ignored by sdist (see MANIFEST.in), used by bdist_wheel
        'browsepy': [
            'templates/*',
            'static/fonts/*',
            'static/*.*', # do not capture directories
        ],
        'browsepy.plugin.player': [
            'templates/*',
            'static/*/*',
        ]},
    install_requires=['Flask>=1.1.2', 'flask_sqlalchemy', 'SQLAlchemy',
        'Flask-Migrate', 'flask_script', 'pycountry'],
    zip_safe=False,
    platforms='any'
)
