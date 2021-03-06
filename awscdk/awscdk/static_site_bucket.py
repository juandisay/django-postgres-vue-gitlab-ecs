import os

from aws_cdk import (
    aws_s3 as s3,
    aws_s3_deployment as s3_deployment,
    aws_iam as iam,
    aws_cloudformation as cloudformation,
    core,
)


class StaticSiteStack(cloudformation.NestedStack):
    def __init__(self, scope: core.Construct, id: str, **kwargs,) -> None:
        super().__init__(scope, id, **kwargs)

        self.static_site_bucket = s3.Bucket(
            self,
            "StaticSiteBucket",
            access_control=s3.BucketAccessControl.PUBLIC_READ,
            bucket_name=f"{scope.full_app_name}-frontend",
            removal_policy=core.RemovalPolicy.DESTROY,
            website_index_document="index.html",
            website_error_document="index.html",
        )

        self.policy_statement = iam.PolicyStatement(
            actions=["s3:GetObject"],
            resources=[f"{self.static_site_bucket.bucket_arn}/*"],
        )

        self.policy_statement.add_any_principal()

        self.static_site_policy_document = iam.PolicyDocument(
            statements=[self.policy_statement]
        )

        self.static_site_bucket.add_to_resource_policy(self.policy_statement)
