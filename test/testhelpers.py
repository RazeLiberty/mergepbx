import os
import logging

TEST_DIR = os.path.dirname(__file__)
FIXTURES_DIR = os.path.join(TEST_DIR, "fixtures")

def fixture_path(path):
    return os.path.join(FIXTURES_DIR, path)

def make_logger(clazz):
    logger_name = "test.%s.%s" % (clazz.__module__, clazz.__name__)
    return logging.getLogger(logger_name)