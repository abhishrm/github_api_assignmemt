Feature: Github
    GitHub API to implement a typical GitHub workflow.

    Scenario: GitHub workflow
        Given user can access existing github account

        When user tries to create repo with name "git_flow_task" appended with suffix current time stamp
        When user creates branch "feature/overall_git_flow_feature"

