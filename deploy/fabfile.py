from fabric.api import *

env.hosts = ['IP_ADDRESS']
env.user = ''
env.password = ''

def deploy():
    try:
        run("cd /path/to/your/site/goes/here/; git pull origin master")
        run("supervisorctl restart gunicorn")
    except:
        pass
