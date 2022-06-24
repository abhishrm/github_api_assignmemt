import os
import configparser

import logging

def initialise_logger():
    logger_name = 'test_framework'
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logfile_name = 'testfile'
    ##Lets create formatter
    formatter = logging.Formatter('%(levelname)s %(name)s %(asctime)s %(module)s %(funcName)s %(message)s')
    ##Lets create file handler
    file_handler = logging.FileHandler(logfile_name)
    # Add formating to file handlere and not the logger
    file_handler.setFormatter(formatter)
    # Now add this handler to logger
    logger.addHandler(file_handler)
    log_console_handler = logging.StreamHandler()
    log_console_handler.setFormatter(formatter)
    logger.addHandler(log_console_handler)
    # logger.info('#############LOGGER CREATED ################## ')
    return logger

def read_config_file(path_config_file):
    """
    This function is to read the config file.
    :param path_config_file: This takes the path of the config file which need to be read.
    :return:
    """
    try:

        config = configparser.ConfigParser()
        config.read(path_config_file)
        return config

    except Exception as e:
        assert False, "Failed to read config file :{}".format(e)

def execute_system_command(command):
    """
    This executes the command on tyhe system
    :param command:
    :return:
    """
    os.system(command)


def change_directory(command):
    """
    This executes the command on tyhe system
    :param command:
    :return:
    """
    os.chdir(command)

