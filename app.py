#!/usr/bin/env python3

from aws_cdk import core

from stacks.pipeline import CompliancePipeline


app = core.App()
CompliancePipeline(app, "compliance-pipeline", env=core.Environment(region="eu-west-1"))

app.synth()
