Python-intercom is a Python wrapper for the `Intercom API <https://api.intercom.io/docs>`_.

Detailed `documentation <http://readthedocs.org/docs/python-intercom/>`_ is available on `http://readthedocs.org <http://readthedocs.org>`_.

Typical usage:

.. code:: python

 from intercom import Intercom
 Intercom.app_id = 'app-id'
 Intercom.api_key = 'api-key'
    
 from intercom import User
 for user in User.all():
     print user.email
