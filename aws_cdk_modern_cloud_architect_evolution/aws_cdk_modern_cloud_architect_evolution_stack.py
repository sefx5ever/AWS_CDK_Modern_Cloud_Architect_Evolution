from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct

class AwsCdkModernCloudArchitectEvolutionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # App 1：EC2 with all default

        ## Select the default vpc
        vpc = ec2.Vpc.from_lookup(self, "VPC",
            vpc_id="vpc-04bc3634aea0e5fc5"                          
        )

        ## Create an EC2 of Amazon Linux 2 Instance 
        ec2.Instance(self, "Instance",
            vpc=vpc,
            instance_type=ec2.InstanceType.of(
                instance_class=ec2.InstanceClass.T3,
                instance_size=ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.MachineImage.latest_amazon_linux2()
        )

