import os
from diazo.wsgi import DiazoMiddleware
from django.core.wsgi import get_wsgi_application
from django.conf import settings

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
#
# default settings 
#     change these settings, if necessary, in DIAZO_CONFIG in your settings file
 
DIAZO_DEFAULTS = dict(
#      app, 
      global_conf={},
      rules='%(THIS_DIR)s/default/rules.xml' % locals(),
      debug=settings.DEBUG,
#      theme=None,
#     prefix=None,
#     includemode='document',
#     debug=False,
#     read_network=False,
#     read_file=True,
#     update_content_length=False,
#     ignored_extensions=(
#         'js', 'css', 'gif', 'jpg', 'jpeg', 'pdf', 'ps', 'doc',
#         'png', 'ico', 'mov', 'mpg', 'mpeg', 'mp3', 'm4a', 'txt',
#         'rtf', 'swf', 'wav', 'zip', 'wmv', 'ppt', 'gz', 'tgz',
#         'jar', 'xls', 'bmp', 'tif', 'tga', 'hqx', 'avi',
#     ),
#     environ_param_map=None,
#     unquoted_params=None,
#     doctype=None,
#     content_type=None,
#     filter_xpath=False,
)

config = DIAZO_DEFAULTS
config.update(settings.DIAZO_CONFIG)

application = DiazoMiddleware(get_wsgi_application(), **config)
