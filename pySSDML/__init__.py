'''
File: __init__.py
Project: pySSDML
File Created: Thursday, 30th July 2020 7:39:08 pm
Author: Sparsh Dutta (sparsh.dtt@gmail.com)
-----
Last Modified: Friday, 31st July 2020 2:26:15 am
Modified By: Sparsh Dutta (sparsh.dtt@gmail.com>)
-----
Copyright 2020 Sparsh Dutta
'''

import os

__version__ = '0.0.1'

# Create output folder for saving logs and artifacts
output_folder_path = os.getcwd().replace("\\",'/')

if os.path.exists(output_folder_path + '/pySSDML_OUTPUT/'):
    pass
else:
    os.mkdir(output_folder_path + '/pySSDML_OUTPUT')