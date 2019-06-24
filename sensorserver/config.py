""" configuration values """


class Config(object):
    DEBUG = True


class DevConfig(Config):
    pass


class ProdConfig(Config):
    pass
