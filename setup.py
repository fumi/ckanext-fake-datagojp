from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-fake-datagojp',
    version=version,
    description="This extension aims to provide files for datago.jp",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Fumihiro Kato',
    author_email='fumi@fumi.me',
    url='http://datago.jp',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.fake_datagojp'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        # myplugin=ckanext.fake-datagojp.plugin:PluginClass
        fake_datagojp_theme=ckanext.fake_datagojp.plugin:FakeDataGoJpThemePlugin
    ''',
)
