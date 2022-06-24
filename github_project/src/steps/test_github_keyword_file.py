from pytest_bdd import scenario, given, when, then
from pytest_bdd import parsers
from datetime import datetime
import pytest
from common_utility.common_utils import *
import os
from pathlib import Path
from sys import platform


FETAURE_FILE_DIRECTORY='features'
feature_file_name = 'github_workflow.feature'
base=str(Path(__file__).resolve().parent)

try:
    base=base.replace('steps','')
except Exception as e:
    assert False, "replace of step strring did not work in :{}".format(base)

if platform == "linux":
    FEATURE_FILE = base + "/" + "features/" + 'github_workflow.feature'

elif platform == "win32":
    FEATURE_FILE= base + "\\" + "features\\" + 'github_workflow.feature'

logger = initialise_logger()

@scenario(FEATURE_FILE, 'GitHub workflow')
def test_github():
    logger.info('##### Scenario Finished #####')


@given("user can access existing github account")
def test_create_Github_API_class_object(create_github_class_object):
    """
    This keyword is to figure out that user can access the GITHUB acount
    :param create_github_class_object:object of github_endpoint class
    :return:
    """

    try:

        response = create_github_class_object.verify_user_can_access_github_account()
        assert response[0]== 200,"Status code not matched expected, received is :{}".format(response[0])
        logger.info('##### Step Passed related to accessing github account #####')

    except Exception as e:
        assert False,"Exccption raised while creating github class object with error :{}".format(str(e))

@when(parsers.cfparse('user tries to create repo with name "{repo_name:string}" appended with suffix current time stamp',extra_types=dict(string=str)))
def create_repo_in_github(create_github_class_object, step_context, repo_name):
    """
    This keyword is used to user defined repository in GITHUB account.
    :param create_github_class_object:object of github_endpoint class
    :param step_context:
    :param repo_name:The user defined repository which need to be created in GITHUB
    :return:
    """
    try:

        repo = repo_name + datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        payload = '{"name": "' + repo + '", "private":false }'
        step_context['response'] = repo
        response = create_github_class_object.create_repository_in_github_account(payload)
        assert response[0] == 201, "Status code not matched expected, received is :{}".format(response[0])
        logger.info('##### Step Passed ralted to creating repository in github account #####')

    except Exception as e:
        assert False, "Exception raised while creating repository in github account with error :{}".format(str(e))


@when(parsers.cfparse('user creates branch "{feature_branch:string}"',extra_types=dict(string=str)))
def user_file(step_context,feature_branch):
    """
    This keyword is implemented to create a branch checkout of the repo created in github.
    And then to add/commit new file to the branch and the push it to the master branch
    :param step_context:
    :param feature_branch:This is the name of the branch which need to be created
    :return:
    """
    try:
##### Reading the data from the config file #####
        path_current_directory = os.path.dirname(__file__)
        path_config_file = path_current_directory + '/configs/commonconfig.ini'
        config = read_config_file(path_config_file)
        repo_path = config['configuration_setting']['repo_path']

##### This is the name of the repo created with time stamp #####
        repo_name = step_context['response']

##### Creating directory and changing the path to create directory where git operations need to be performed #####
        os.chdir(repo_path)
        create_directory_command = "mkdir " + repo_name
        execute_system_command(create_directory_command)
        change_directory(repo_path + repo_name)

##### GIT opeartions in sequence #####
        execute_system_command("git init")
        github_user_account_url= "https://github.com/abhishrm/"
        remote_command = "git remote add origin " + github_user_account_url + repo_name + ".git"
        execute_system_command(remote_command)
        execute_system_command("git checkout -b " +  feature_branch)
        execute_system_command("echo '# " + repo_name + "' >>README.md")
        execute_system_command("git add *")
        execute_system_command("git commit -m " + "'"+ feature_branch + "'"+ '"')
        execute_system_command("git push origin " + feature_branch)

        logger.info('##### Step Passed related to creating branch/commiting code and pushing code to master #####')

    except Exception as e:
        assert False, "Exception raised while performing GIT operations with error :{}".format(str(e))




