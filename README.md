# dog-facts
A Discord bot that responds with random facts about dogs.

This was a fun little project to I used to get introduced to AWS CodeDeploy. You can see the appspec.yml file which tells CodeDeploy the script to copy for the bot to run, then a handful of shell scripts make sure dependencies are installed, start the bot, and stop it.

To do:
 - Add GitHub actions to push to CodeDeploy / EC2
 - Add support for adding to multiple Discord servers?
 - Possibly convert .env / loadenv functionality for Discord Token to native boto3 / AWS solution
 - Package it so it can be cloned + redeployed by others
