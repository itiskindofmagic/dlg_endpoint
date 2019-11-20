class Config(object):
    pass
    # placeholder for more general settings, paths etc.


class DevConfig(Config):
    ENV = 'dev'
    PORT = 5000
    DEBUG = True
    NUMBERS = list(range(10000001))


class TestConfig(Config):
    ENV = 'test'
    PORT = 5000
    DEBUG = True
    TESTING = True
    NUMBERS = list(range(3))
