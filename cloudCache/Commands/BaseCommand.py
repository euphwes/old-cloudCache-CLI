""" The base command class which all other commands subclass. """

import sys, json, requests, arrow
from cloudCache.Constants import CFG_SERVER, CFG_PORT, CFG_USER, CFG_API_KEY, CFG_ACCESS_TOKEN, CFG_TOKEN_EXPIRES

# -------------------------------------------------------------------------------------------------

class BaseCommand(object):
    """ The base command class. """

    def __init__(self, args, config_file):
        self.args = args
        self.config_file = config_file
        self._validate_args()


    def _validate_args(self):
        """ Any subclasses must implement this method. Validate the args passed into the
        constructor and verify they are appropriate for this command, and complete. """
        raise NotImplementedError()


    @property
    def url(self):
        """ Any subclass must implement this property. Return the API endpoint URL which this
        command uses, based on args and configuration. """
        raise NotImplementedError()


    @property
    def base_url(self):
        """ Build and return the base URL for the API endpoints. """
        return 'http://{}:{}'.format(self.config[CFG_SERVER], self.config[CFG_PORT])
