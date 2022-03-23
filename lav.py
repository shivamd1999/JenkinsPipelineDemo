
    
import jenkinsapi
from jenkinsapi.jenkins import Jenkins
server = Jenkins(jenkins_url='http://localhost:8080/job/Task_1/',username='shivamd1',password='CzpW8Wy9')
print(server.get_job("Task_1").get_last_buildnumber())
