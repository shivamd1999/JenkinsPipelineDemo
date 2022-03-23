import jenkins
import urllib2 
import urllib
import sys

j = jenkins.Jenkins('http://localhost:8080')
if not j.job_exists('Task_1'):
    j.create_job('Task_1', jenkins.EMPTY_CONFIG_XML)

j.reconfig_job('Task_1', jenkins.RECONFIG_XML)
j.build_job('Task_1')


build_info=j.get_build_info('Task_1')
if build_info['result']=='SUCCESS':
    print "Build Success "
else:
    print " Build Failed "
