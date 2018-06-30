# Definition of the tags that are automatically assigned to tasks with given
# projects when created.
TAGS_FOR_PROJECTS = { 'a_private_project': ['private'],
                      'a_job_project_with_foo': ['job', 'foo'],
                     }

def hook_tags_for_projects(task):
    """ taskpirate-enabled hook to automatically
    assign tags to certain projects """
    if task['project'] in TAGS_FOR_PROJECTS.keys():
        for tag in TAGS_FOR_PROJECTS[task['project']]:
            task['tags'].add(tag)
