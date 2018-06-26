import logging
import click
from logging import Formatter, StreamHandler


class ClickHandler(StreamHandler):
    """
    This is a derived class of implemented logging class
    which overrides some of its functional definitions to add
    color to the StreamHandler
    """
    def emit(self, record):
        colormap = {
            'DEBUG': ('white', 'black'),
            'INFO': ('cyan', None),
            'WARNING': ('yellow', None),
            'ERROR': ('red', None),
            'CRITICAL': ('white', 'red'),
        }
        try:
            msg = self.format(record)
            colors = colormap.get(record.levelname, (None, None))
            fgcolor = colors[0]
            bgcolor = colors[1]
            click.secho(msg, fg=fgcolor, bg=bgcolor)
            self.flush()
        except Exception:
            self.handleError(record)

logger = logging.getLogger(__name__)
handler = ClickHandler()
logger.addHandler(handler)

if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)
    logger.debug('This is for debug level')
    logger.info('This is for info level')
    logger.warning('This is for warning level')
    logger.error('This is for error level')
    logger.critical('This is for critical level')
