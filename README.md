# AWSLambdaCICD
There are 4 stages in the pipeline,
1. Source repository 
	- CodeCommit, GitHub, GitLab etc.

2. Build - CodeBuild
	- References buildspec.yaml
	- Create outputTemplate.yaml using template.yml
	- Create CloudFormation Stack

3. Create or replace ChangeSet (CloudFormation)
	- references outputTemplate.yaml

4. Execute ChangeSet (CloudFormation)

