import jenkins
import time
import getpass
import argparse
import constants

class DevOpsJenkins:
    def __init__(self, JENKINS_URL, JENKINS_USERNAME, JENKINS_PASSWORD):
        self.jenkins_server = jenkins.Jenkins(JENKINS_URL,
                                              username=JENKINS_USERNAME,
                                              password=JENKINS_PASSWORD)

    def build_job(self, name, parameters=None, token=None):
        next_build_number = self.jenkins_server.get_job_info(name)['nextBuildNumber']
        self.jenkins_server.build_job(name, parameters=parameters, token=token)
        time.sleep(10)
        build_info = self.jenkins_server.get_build_info(name, next_build_number)
        return build_info

if __name__ == "__main__":
    # Enter your inputs here
    
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument('--x', type=str, default='X_value', help='Mention the X value')
    parser.add_argument('--y', type=str, default='Y_value', help='Mention the Y value')
    parser.add_argument('--z', type=str, default='Z_value', help='Mention tthe Z value')
    
    # Read arguments from command line
    args = parser.parse_args()

    PARAMETERS = {'X': args.x,
                  'Y': args.y,
                  'Z': args.z,
                  }

    # Get the user inputs
    JENKINS_PORT = input("Enter the Jenkins port number: \t")
    JENKINS_URL = "http://localhost:" + JENKINS_PORT
    JENKINS_USERNAME = input("Enter the Jenkins username: \t")
    JENKINS_PASSWORD = getpass.getpass(prompt='Enter the Jenkins password: \t')
    NAME_OF_JOB = input("Enter the Jenkins job name: \t")
    TOKEN_NAME = getpass.getpass(prompt='Enter the Jenkins token: \t')

    jenkins_obj = DevOpsJenkins(JENKINS_URL, JENKINS_USERNAME, JENKINS_PASSWORD)
    output = jenkins_obj.build_job(NAME_OF_JOB, PARAMETERS, TOKEN_NAME)
    print("Jenkins Build URL: {}".format(output['url']))
