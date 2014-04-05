''' plugin.py
'''
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class FakeDataGoJpThemePlugin(plugins.SingletonPlugin):
  '''
    CKAN theme plugin for datago.jp
  '''
  plugins.implements(plugins.IConfigurer)

  def update_config(self, config):
    toolkit.add_template_directory(config, 'templates')
    toolkit.add_public_directory(config, 'public')
