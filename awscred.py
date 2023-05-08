#!/usr/bin/env python3

import sys
import configparser
from pathlib import Path

"""
The purpose of this script is to make it easy to list and switch
between AWS profiles.  It does this by reading the AWS credentials
file in the AWS_CREDENTIALS_FILE variable and, depending on the
parameter, either listing the profiles or switching to a new profile.
Usage:
    awscred.py  
        - Lists all profiles in the AWS credentials file.
    awscred.py [profile] 
        - Switches the default profile to [profile].
"""

# this is the default location of the AWS credentials file
# if you want to use a different location, change this variable
# to point to the correct location
AWS_CREDENTIALS_FILE = str(Path.home()) + '/.aws/credentials'

# now we're going to read the AWS credentials from the file specified
# above and store them in a dictionary. If the file doesn't exist,
# we'll exit with an error message
try:
    config = configparser.ConfigParser()
    config.read(AWS_CREDENTIALS_FILE)
except FileNotFoundError:
    print('AWS credentials file not found at ' + AWS_CREDENTIALS_FILE)
    exit(1)

# if the user didn't specify a profile, we'll just list all the
# profiles in the AWS credentials file
if len(sys.argv) == 1:
    print('Available AWS profiles:')
    for section in config.sections():
        print('  ' + section)
    exit(0)

# The user specified a profile, so we'll switch to that profile
# if it exists. If it doesn't exist, we'll exit with an error
# message.
if len(sys.argv) == 2:
    profile = sys.argv[1]
    if profile not in config.sections():
        print('Profile ' + profile + ' not found in ' + AWS_CREDENTIALS_FILE)
        exit(1)
    print('Switching to profile ' + profile)
    config['default'] = config[profile]
    with open(AWS_CREDENTIALS_FILE, 'w') as configfile:
        config.write(configfile)
    exit(0)
