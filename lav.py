

info = server.get_job_info('Task_1')

# Loop over builds
builds = info['builds']
for build in builds:
    for build in builds:
        print(server.get_build_info('Task_1', 
                                    build['number']))
