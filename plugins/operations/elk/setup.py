# Copyright 2016, IBM US, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

setup(
    name='opsmgr-plugins-operations-elk',
    version='0.1',

    description='Operational Management Operations Plugin for ELK',

    author='',
    author_email='',

    url='',

    classifiers=[
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 ],

    platforms=['Any'],

    scripts=[],

    namespace_packages=['opsmgr','opsmgr.plugins','opsmgr.plugins.operations'],

    provides=['opsmgr.plugins.operations.elk'],

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'opsmgr.inventory.interfaces.IOperationsPlugin': [
            'ELK = opsmgr.plugins.operations.elk.ELKOperationsPlugin:ELKPlugin',
        ],
    },

    zip_safe=False,
)

