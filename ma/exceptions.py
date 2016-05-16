class MissingUtilityHashError(Exception):
    def __init__(self, source):
        message = "No utility hash present, cannot execute. Context: [{}]".format(source)
        Exception.__init__(self, message)
