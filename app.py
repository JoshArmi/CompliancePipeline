#!/usr/bin/env python3

from aws_cdk import core

from compliance_pipeline.compliance_pipeline_stack import CompliancePipelineStack


app = core.App()
CompliancePipelineStack(app, "compliance-pipeline")

app.synth()
