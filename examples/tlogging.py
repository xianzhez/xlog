import logging

logger = logging.getLogger()

print('logger', logger.getEffectiveLevel())
logger.debug('debug 1')

logger.setLevel(logging.NOTSET)
logger.debug('debug 2')

logger.critical('critical 1')

import logging
logger = logging.getLogger('something')
myFormatter = logging.Formatter('%(asctime)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(myFormatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.info("log statement here")

#Tweak the formatter
myFormatter._fmt = "My PREFIX -- " + myFormatter._fmt
logger.info("another log statement here")