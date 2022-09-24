import logging
import time


def get_logger():
    logging.basicConfig(level=logging.INFO, filename=time.strftime("my-%Y-%m-%d.log"), format='%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s')

    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")


if __name__ == '__main__':
     get_logger()
