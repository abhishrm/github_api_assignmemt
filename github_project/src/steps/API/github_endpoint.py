import logging
import requests
from common_utility.common_utils import *



class GithubEndpoint():

    def __init__(self):
        self.logger = initialise_logger()
        self.github_url = "https://api.github.com/"
        self.create_rep_url = self.github_url + "user/repos"
        self.headers = {'Authorization': 'token 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', 'Accept': 'application/vnd.github.v3+json'}
        self.token = {"oidc_id_token":"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"}

    def verify_user_can_access_github_account(self):
        """
        This function is used to check whether user can call Github using GET endpoint
        :param self:
        :return:endpoint response status code and response text as tuple.
        """
        response = requests.get(self.github_url,  headers=self.headers)
        self.logger.info('get status code: %s' % response.status_code)
        self.logger.info('get text : %s' % response.text)
        return response.status_code, response.json()

    def create_repository_in_github_account(self,payload):
        """
        This function is use to create repository in GITHUB account.
        :param payload: payload required to make POST call.
        :return: endpoint response status code and response text as tuple.
        """
        response = requests.post(self.create_rep_url,data=payload, headers=self.headers)
        self.logger.info('get status code: %s' % response.status_code)
        self.logger.info('get text : %s' % response.text)
        return response.status_code, response.json()

