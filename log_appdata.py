import logging
from logging_gelf.formatters import GELFFormatter
from logging_gelf.handlers import GELFTCPSocketHandler

logger = logging.getLogger("gelf")
# set the log level

logger.setLevel (logging.DEBUG)

# set the host name and port number of the remote logging server 
handler = GELFTCPSocketHandler(host="127.0.0.1", port=12201) 
handler.setFormatter(GELFFormatter(null_character=True)) 
logger.addHandler(handler)

#debug, info, warning, error, critical
logger.debug("debug!")

logger.warning("warning!")

logger.error("There was an error!")

logger.critical("There was a critical error!")