# Github workflow automation

# How to run complete project using Docker:

-Clone the repository using command -> git clone https://github.com/abhishrm/github_api_assignmemt.git

-Navigate to project path on command line -> /github_project/

-This folder directory i.e. github_project contains bash script with name -> "build_and_run.sh"

-You need to run this bash script by passing only one mandatory command line parameter. The parameter should be the name with which you want to build the image.

-If you do not pass this parameter, then this bash script will exit and will provide you instructions about passing a mandatory command line argument.

-Run this bash script by writing and then enter-> ./build_and_run.sh <user_defined_name_need_to_be_passed>

-This bash script while running will create the image and will run the container .

-Also it will install all the dependencies required to run the test i.e. all python libraries from the requirements.txt file.

-Also it will automatically trigger the pytest bdd scenario and will generate a test report with convention report.html.

-There is no such manual intervention required. You only need to trigger bash script "build_and_run.sh"


# How to run the test locally by creating a virtual environment cloning the repository

-Install virtualenv by passing command "pip install virtualenv".

-Now create a virtualenv using the following command: virtualenv <here_pass_name_of_the_virtual_environment>
 After running this command, a directory named <here_pass_name_of_the_virtual_environment> will be created. This is the directory which contains all the necessary executables to use the packages that a Python project would need. This is where Python packages will be installed.

-Specify Python interpreter of your choice using command -> virtualenv -p /usr/bin/python3 virtualenv_name

-Now after creating virtual environment, you need to activate it.
 To do this run command -> "source virtualenv_name/bin/activate"
 Once the virtual environment is activated, the name of your virtual environment will appear on left side of terminal. This will let you know that the virtual environment is currently active

-Now clone the code from git clone https://github.com/abhishrm/github_api_assignmemt.git
-Now you can install dependencies by navigating to github_project directory.
 This directory contains all dependencies in "requirements.txt"
 Install all dependencies by running command : pip install -r ./requirements.txt
 
-Navigate to the project path folder on the command line -> /github_project/src/steps. 
-Under step folder run the command like -> pytest -s -v test_github_keyword_file.py -s -v --html=github_result.html

On windows command prompt it looks like,

     C:/Users/Abhishek/Downloads/github_project/src/steps>pytest test_github_keyword_file.py -s -v --html=github_result.html

     where: 'github_project' is a directory where we check out automation code from repo
     
-You will find user friendly test report formed as github_result.html. You can open this html link to view the test result.

-Once you are done with the work, you can deactivate the virtual environment by the following command:deactivate
