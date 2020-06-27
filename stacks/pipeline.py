from aws_cdk import core
from aws_cdk.aws_codebuild import PipelineProject
from aws_cdk.aws_codecommit import Repository
from aws_cdk.aws_codepipeline import Artifact, Pipeline
from aws_cdk.aws_codepipeline_actions import CodeBuildAction, CodeCommitSourceAction
from aws_cdk.aws_iam import Policy, PolicyStatement, Role, ServicePrincipal


class CompliancePipeline(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        repo = Repository(self, "Repository", repository_name="CompliancePipeline")
        my_pipeline = Pipeline(self, "Pipeline")

        # add a stage
        source_stage = my_pipeline.add_stage(stage_name="Source")

        output = Artifact()

        # add a source action to the stage
        source_stage.add_action(
            CodeCommitSourceAction(action_name="Source", output=output, repository=repo)
        )

        deploy = my_pipeline.add_stage(stage_name="AdministerPipeline")

        policy = Policy(
            self,
            "CodeBuildPolicy",
            statements=[PolicyStatement(actions=["*"], resources=["*"])],
        )

        role = Role(
            self,
            id="CodeBuildRole",
            assumed_by=ServicePrincipal("codebuild.amazonaws.com"),
            managed_policies=[policy],
        )

        project = PipelineProject(self, id="PipelineBuild", role=role)

        deploy.add_action(
            CodeBuildAction(
                action_name="AdministerPipeline", input=output, project=project
            )
        )

