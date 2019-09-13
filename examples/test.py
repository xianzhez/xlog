import sys
sys.path.insert(0, "../../")
import xlog
import logging
import time

# logging.getLogger()

from inspect import currentframe, getframeinfo

def getlineno():
    return getframeinfo(sys._getframe(1) if hasattr(sys, "_getframe") else None)

frameinfo = getframeinfo(currentframe())
tinfo = getlineno()

print(frameinfo.filename, frameinfo.lineno)

print(tinfo.filename, tinfo.lineno)
print(tinfo)

# logging.getLogger().setLevel(xlog.WARNING)

xlogger = xlog.getLogger()
xlogger.setLevel(xlog.NOTSET)
xlogger.log('hello xlog')
xlogger.configure_format(lineno=True, funcName=True, filename=True)


for i in range(10):
    time.sleep(0.1)
    xlogger.log('{}/{}'.format(i+1, 10), update=True)

xlogger.log('Done1 %s', 'test format')
xlogger.log('Done2')
xlogger.log('Done3')
xlogger.debug('Debug log')
# print(xlogger.getEffectiveLevel())
# print(logging.root.handlers)
# print(xlogger == logging.root)


# print(xlogger.fakemethod())

