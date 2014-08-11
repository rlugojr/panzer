# Exception classes

class Error(Exception):
    """ base class for all panzer exceptions """
    pass

class SetupError(Error):
    """ error in the setup phase """
    pass

class BadASTError(PanzerError):
    """ malformatted AST encountered (e.g. C or T fields missing) """
    pass

class KeyError(PanzerError):
    """ looked for metadata field, did not find it """
    pass

class TypeError(PanzerError):
    """ looked for value of a type, encountered different type """
    pass

class InternalError(PanzerError):
    """ function invoked with invalid parameters """
    pass

