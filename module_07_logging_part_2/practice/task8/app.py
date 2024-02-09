import logging, logging.handlers
import json


class myHTTPHandler(logging.handlers.HTTPHandler):
    def mapLogRecord(self, record):
        trec = {'record': json.dumps(record.__dict__)}
        return trec


myLogger = logging.getLogger('MTEST')
myLogger.setLevel(logging.DEBUG)
httpHandler = myHTTPHandler('localhost:3500', url='/log', method="POST")
myLogger.addHandler(httpHandler)

myLogger.info('Small info message')
myLogger.debug('Small debug message')
myLogger.error('Small error message')
