

#!/usr/bin/env python3
# author: @netmanchris

"""
Copyright 2016 Hewlett Packard Enterprise Development LP.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

""" This file will take the GET the contents of the HPE IMC Network Assets module and dump them into a CSV file called
all_assets.csv where each line of the CSV file represents one physical or logical asset as discovered by the HPE IMC
platform.


 This library uses the pyhpeimc python wrapper around the IMC RESTful API to automatically push the new performance tasks
 with minimal effort on the part of the user."""

import csv
from pyhpeimc.auth import *
from pyhpeimc.plat.netassets import *

auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")


all_assets = get_dev_asset_details_all(auth.creds, auth.url)

keys = all_assets[0].keys()

for i in all_assets:
    if len(i) != len(all_assets[0].keys()):
        keys = all_assets[all_assets.index(i)].keys()

with open ('all_assets.csv', 'w') as file:
    dict_writer = csv.DictWriter(file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_assets)




