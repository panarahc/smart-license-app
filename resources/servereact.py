# Copyright (c) 2019 Cisco and/or its affiliates.
#
# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.1 (the "License"). You may obtain a copy of the
# License at
#
#                https://developer.cisco.com/docs/licenses
#
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

from flask_restful import Resource
from flask import send_from_directory
import os.path


class Servereact(Resource):
    def get(self, path):
        if path != "" and os.path.exists("frontend/build/" + path):
            return send_from_directory('frontend/build', path)
        else:
            return send_from_directory('frontend/build', 'index.html')
