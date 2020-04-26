from service import start_service
import logging

log = logging.getLogger("ocr")
log.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('ocr.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter(fmt='%(asctime)s [%(levelname)s @ %(name)s (%(threadName)s)] => %(message)s', datefmt='%Y_%m_%d %H:%M:%S')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
log.addHandler(fh)
log.addHandler(ch)

start_service()
