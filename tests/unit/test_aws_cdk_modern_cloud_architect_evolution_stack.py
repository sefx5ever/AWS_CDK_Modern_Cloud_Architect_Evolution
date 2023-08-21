import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_modern_cloud_architect_evolution.aws_cdk_modern_cloud_architect_evolution_stack import AwsCdkModernCloudArchitectEvolutionStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_modern_cloud_architect_evolution/aws_cdk_modern_cloud_architect_evolution_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkModernCloudArchitectEvolutionStack(app, "aws-cdk-modern-cloud-architect-evolution")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
