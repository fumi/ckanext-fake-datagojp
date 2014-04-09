ckanext-fake-datagojp
====================

CKAN extension for datago.jp

# Install

```
$ pip install -e git+https://github.com/fumi/ckanext-fake-datagojp.git#egg=ckanext-fake-datagojp
```
Add fake_datagojp_theme into ckan.plugins in your configuration file.

```
ckan.plugins = stats text_preview recline_preview pdf_preview fake_datagojp_theme
```

Then restart your web server.
