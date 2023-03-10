from .base import *
# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
# if config("DEVELOPMENT_STATE") == 'True':
#    from .dev import *
# else:
#    from .prod import *
   
if os.getenv('DJANGO_DEVELOPMENT') == 'true':
   from .dev import *
else:
   from .prod import *