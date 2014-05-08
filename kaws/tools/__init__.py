from kaws.tools.aws import AwsCliTool
from kaws.tools.autoscale import AutoScaleTool
from kaws.tools.cloudformation import CloudFormationTool
from kaws.tools.cloudwatch import CloudWatchTool
from kaws.tools.ec2ami import Ec2AmiTool
from kaws.tools.ec2api import Ec2ApiTool
from kaws.tools.elasticache import ElasticacheTool
from kaws.tools.elb import ElbTool
from kaws.tools.iam import IamTool
from kaws.tools.rds import RdsTool
from kaws.tools.s3cmd import S3CmdTool

def get_tools():
	return [
		AwsCliTool(),
		AutoScaleTool(),
		CloudFormationTool(),
		CloudWatchTool(),
		Ec2AmiTool(),
		Ec2ApiTool(),
		ElasticacheTool(),
		ElbTool(),
		IamTool(),
		RdsTool(),
		S3CmdTool()]

