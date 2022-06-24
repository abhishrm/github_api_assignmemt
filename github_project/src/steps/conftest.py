import pytest
from API.github_endpoint import GithubEndpoint


@pytest.fixture
def create_github_class_object():
    """This Function create the object of class GithubEndpoint and then returns it """
    return GithubEndpoint()

@pytest.fixture
def step_context():
    return {'response': None}

