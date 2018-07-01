#! /usr/bin/python
import sys
import boto3
import time

stack_name = sys.argv[1]
REGION = sys.argv[2]
LAYER = sys.argv[3]

iam = boto3.client('iam')
client = boto3.client('opsworks', region_name=REGION)
stacks = client.describe_stacks()
# layers = client.describe_layers(stacks)


def get_stack_id(stack_name):
    for d_stack in stacks['Stacks']:
        if d_stack['Name'] == stack_name:
            # print "matching stacks : " + d_stack['Name']
            return d_stack['StackId'P]


def get_layer_id(stackid):
    stackid = get_stack_id(stack_name)
    stack_layers = client.describe_layers(StackId=stackid)
    for d_layer in stack_layers['Layers']:
        if d_layer['Name'] == LAYER:
            # print d_layer['LayerId']
            return d_layer['LayerId']


def get_opsworks_instance_ids(stackid):
    old_instances = []
    layer_instances = client.describe_instances(LayerId=get_layer_id(stackid))
    for d_instance in layer_instances['Instances']:
        old_instances.append(d_instance['InstanceId'])
        continue
    return old_instances


def create_instances(instance_dict):
    layer_instances = client.describe_instances(LayerId=get_layer_id(stackid))
    instance_dict = layer_instances['Instances'][-1]
    base_instance_dict = {
        'AmiId': 'ami-3e346142',
        'InstanceType': 'm4.10xlarge',
        'LayerIds': ['95f13bcf'],
        'Os': 'Custom',
        'SshKeyName': 'gsk',
        'StackId': 'd0f9a991608b',
        'SubnetId': 'abc123'
    }
    new_instances = []
    for count in range(len(get_opsworks_instance_ids(stackid))):
        response = client.create_instance(
            StackId=get_stack_id(stack_name),
            LayerIds=[get_layer_id(stackid)],
            InstanceType=base_instance_dict['InstanceType'],
            SubnetId=base_instance_dict['SubnetId'],
            SshKeyName=base_instance_dict['SshKeyName'],
            StackId=base_instance_dict['StackId'],
            Os=base_instance_dict['Os'],
            AmiId=base_instance_dict['AmiId']
        )
        return new_instances.append(response['InstanceId'])


def replace_instances(layer):
    for instance_id in create_instances(instance_id):
        response = client.start_instance(InstanceId=instance_id)
        stop_old_instances(instance_id)
        return response
        time.sleep(600)


def stop_old_instances(instance_id):
    for instance_id in get_opsworks_instance_ids(stackid):
        response = client.stop_instance(
            InstanceId='string',
            Force=False,
        )
        return response


if __name__ == '__main__':
    print get_stack_id(stack_name)
    stackid = get_stack_id(stack_name)
    print get_layer_id(stackid)
    print get_opsworks_instance_ids(stackid)
