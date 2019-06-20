import pkg_resources

try:
    __version__ = pkg_resources.get_distribution('remail').version
except:
    __version__ = 'not installed'
