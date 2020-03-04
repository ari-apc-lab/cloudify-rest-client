########
# Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

from setuptools import setup, find_packages

setup(
    name='cloudify_rest_client',
    version='4.4.dev1',
    author='cosmo-admin',
    author_email='cosmo-admin@gigaspaces.com',
    packages=find_packages(include=['cloudify_rest_client*']),
    license='LICENSE',
    description='Cloudify REST client',
    install_requires=[
        'requests>=2.7.0,<3.0.0',
        'requests_toolbelt',
    ]
)
