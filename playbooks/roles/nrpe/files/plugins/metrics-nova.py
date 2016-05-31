#!/usr/bin/env python


# This plugin gives information about the hypervisors. It works as is if using Python2.7 but to get it working with Python2.6 and
# before (as well as Python 3.0) require that you number the placeholders in the format method().
# This way wherever the {} is used, number it starting from 0. e.g., {0}.nova.hypervisor

# #RED
from argparse import ArgumentParser
import socket
import time
import os

from novaclient.client import Client

DEFAULT_SCHEME = '{}.nova.hypervisors'.format(socket.gethostname())

METRIC_KEYS = (
    'current_workload',
    'disk_available_least',
    'local_gb',
    'local_gb_used',
    'memory_mb',
    'memory_mb_used',
    'running_vms',
    'vcpus',
    'vcpus_used',
)

def output_metric(name, value):
    print '{}\t{}\t{}'.format(name, value, int(time.time()))

def main():
    parser = ArgumentParser()
    parser.add_argument('-u', '--user', default=os.environ['OS_USERNAME'])
    parser.add_argument('-p', '--password', default=os.environ['OS_PASSWORD'])
    parser.add_argument('-t', '--tenant', default=os.environ['OS_TENANT_NAME'])
    parser.add_argument('-a', '--auth-url', default=os.environ['OS_AUTH_URL'])
    parser.add_argument('-S', '--service-type', default='compute')
    parser.add_argument('-H', '--host')
    parser.add_argument('-s', '--scheme', default=DEFAULT_SCHEME)
    args = parser.parse_args()

    args.user

    client = Client(version=2, username=args.user, api_key=args.password,
                    project_id=args.tenant, auth_url=args.auth_url,
                    service_type=args.service_type)

    if args.host:
        hypervisors = client.hypervisors.search(args.host)
    else:
        hypervisors = client.hypervisors.list()

    for hv in hypervisors:
        hostname = hv.hypervisor_hostname.split('.')[0]
        for key, value in hv.to_dict().iteritems():
            if key in METRIC_KEYS:
                output_metric('{}.{}.{}'.format(args.scheme, hostname, key), value)

if __name__ == '__main__':
    main()
