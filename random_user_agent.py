import random
import os
import gettext

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

# Translation stuff
gettext.install('w3af', os.path.join(ROOT_PATH, 'locales'))

UA_CACHE = []
UA_FILE = os.path.join(ROOT_PATH, 'core', 'data', 'user_agent',
                       'user-agent-list.txt')


def get_random_user_agent(agent_list=UA_CACHE):
    if not len(agent_list):
        ua_file = file(UA_FILE)

        for line in ua_file:
            line = line.strip()

            if line:
                agent_list.append(line)

    ua = random.choice(UA_CACHE)
    return ua
