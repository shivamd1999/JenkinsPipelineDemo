
import jenkinsapi
from jenkinsapi import jenkins
ci_jenkins_url = "https://http://localhost:8080/job/Task_1/"
username = "shivamd1"
token = "CzpW8Wy9"
job = "Task_1"
j = jenkins.Jenkins(ci_jenkins_url, username=username, password=token)

if __name__ == "__main__":
    j.build_job(job)
