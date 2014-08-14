"""

:synopsis: Specialized Parser classes for Metasploit.

.. moduleauthor:: Tao Sauvage

"""

from libptp.parser import FileParser
from libptp.tools.metasploit.signatures import SIGNATURES


class MetasploitParser(FileParser):
    """Metasploit specialized parser."""

    #: :class:`str` -- Name of the tool.
    __tool__ = 'metasploit'
    #: :class:`str` -- Format of Metasploit reports it supports.
    __format__ = 'metasploit'
    #: :class:`list` -- Metasploit versions it supports.
    __version__ = ['']
    #: :class:`str` -- Metasploit plugin full name.
    __plugin__ = ''

    def __init__(self, fullpath, plugin=''):
        FileParser.__init__(self, fullpath)
        self.__plugin__ = plugin

    # TODO: Properly check the supported versions.
    @classmethod
    def is_mine(cls, fullpath, plugin=''):
        if plugin:
            return True
        return False

    # TODO: Properly retrieve the metadatas.
    def parse_metadata(self):
        return {}

    def parse_report(self):
        """Parser the results of a Metasploit plugin.

        :return: List of dicts where each one represents a vuln.
        :rtype: :class:`list`

        """
        try:
            signatures = SIGNATURES.get(self.__plugin__, {}).iteritems()
        except AttributeError:  # Python3
            signatures = SIGNATURES.get(self.__plugin__, {}).items()
        self.vulns = [{
            'name': self.__plugin__,
            'ranking': ranking}
            for signature, ranking in signatures
            if signature in self.stream]
        return self.vulns
