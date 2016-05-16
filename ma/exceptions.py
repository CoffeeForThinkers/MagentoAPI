class MissingSecurityTokenError(Exception):
    def __init__(self, source):
        message = "No Magento security token present, cannot execute. Context: [{}]".format(source)
        super(MissingSecurityTokenError, self).__init__(message)
