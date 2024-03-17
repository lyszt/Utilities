import json
import os
import sys

# CONFIG
FOLLOWERS_FILE = 'put_list_here/followers_1.json'
FOLLOWINGS_FILE = 'put_list_here/following.json'

if __name__ == '__main__':
    if not ((os.path.isfile(FOLLOWINGS_FILE) and os.access(FOLLOWINGS_FILE, os.R_OK))
            or not (os.path.isfile(FOLLOWERS_FILE) and os.access(FOLLOWERS_FILE, os.R_OK))):
        print("Please insert the required files on 'put_list_here'.")
        sys.exit()

    with open(FOLLOWERS_FILE, "r") as followers_f, open(FOLLOWINGS_FILE, "r") as followings_f:
        followers_f = json.load(followers_f)
        followings_f = json.load(followings_f)
        print(len(followings_f["relationships_following"]))
        followers_list = []

        for item in followers_f:
            target = item['string_list_data'][0]['value']
            followers_list.append(target)
        for item in followings_f["relationships_following"]:
            target = item['string_list_data'][0]['value']
            if target not in followers_list:
                print(target)
