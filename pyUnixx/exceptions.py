
"""
Exceptions which can be raised by py-Unixx Itself.
"""


class pyUnixxError(Exception):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pyUnixxError):
    ...
