'''
The Terminal Class is used to run the pokerbot in terminal mode without a GUI. This is useful for pokerbot tournaments
where the bot is run on a server and no OCR is needed
'''
import logging


class Terminal(object):
    def __init__(self):
        self.active = False


    class statusbar(object):
        def set(value):
            logger.info("Status: "+str(value))

    class var0(object):
        def set(value):
            logger.info(value)

    class var1(object):
        def set(value):
            logger.info(value)

    class var2(object):
        def set(value):
            logger.info(value)

    class var3(object):
        def set(value):
            logger.info(value)

    class var4(object):
        def set(value):
            logger.info(value)

    class var5(object):
        def set(value):
            logger.info(value)

    class var6(object):
        def set(value):
            logger.info(value)


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)