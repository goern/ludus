# ludus
Ludus is a gamification framework for Github and Trello. It can also be extended to other version control and project management tools like Gitlab, Jira etc. This application has been configured with 11 events and 15 badges currently. You can design and contribute more events or badges as per your needs.</br> 
The Ludus project is sponsered by **Red Hat Inc**. As a part of **Red Hat** AICoE under Team AIOps this project was completed as the Summer Internship project.

## Motivation

According to TalentLMS Gamification at Work Survey 2018, about 85 % of employees agreed that they would spend more time on the gamified software. Our motivation behind Ludus is to bring a positive transformation in the software industry by the gamification of Version Control and Project Tracking tools.

## Architecture

![architecture](/docs/architecture.png)

For more information on the Open Data Hub architecture go [here](https://opendatahub.io/news/2018-12-04/open-data-hub-overview.html)

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live OpenShift Cluster.

### Deployment

- To deploy the event listener application on openshift use following command
	'''
	oc process -f openshift/ludus.event_listener.deployment.template.yaml -p GITHUB_URL=<github_url> KAFKA_TOPIC=<kafka_topic_name> KAFKA_BOOTSTRAP_SERVER=<kafka_bootstrap_server>| oc apply -f -
	'''

	<github_url>             : The url of the forked github repository of ludus. The default is 'https://github.com/akhil-rane/Ludus.git'
	<kafka_topic_name>       : The name of the kafka topic where event lister will publish the incoming events
	<kafka_bootstrap_server> : The hostname and port of the the kafka bootstrap server. The valid format is hostname:port


- To deploy the awarder application on openshift use following command
	'''
	oc process -f openshift/ludus.awarder.deployment.template.yaml -p GITHUB_URL=<github_url> KAFKA_TOPIC=<kafka_topic_name> KAFKA_BOOTSTRAP_SERVER=<kafka_bootstrap_server> AWARDER_NAME=<awarder_name> AWARDER_PORT=<awarder_port> EVENTS_TABLE_NAME=<events_table_name> BADGES_TABLE_NAME=<badges_table_name> | oc apply -f -
	'''

	<github_url>             : The url of the forked github repository of ludus. The default is 'https://github.com/akhil-rane/Ludus.git'
        <kafka_topic_name>       : The name of the kafka topic where event lister will publish the incoming events
        <kafka_bootstrap_server> : The hostname and port of the the kafka bootstrap server. The valid format is hostname:port
	<awarder_name>           : The name of the awarder application. This should be unique per kafka cluster. You can scale it to distribute event processing load
	<awarder_port> 		 : The port number of the awarder application
        <events_table_name>      : The table where events data of the user will be stored by awarder. This should be unique per kafka cluster.
        <badges_table_name>      : The table where all previously awarded badges for the user will stored by the awarder.This should be unique per kafka cluster

### How to configure github and trello webhooks?

### How to configure new events and badges?

## Built With

* Python 
* Flask
* Kafka
* Faust
* Elasticsearch
* Kibana
* Docker 
* OpenShift

## Credits

* [AICoE](https://github.com/AICoE)
* [Open Data Hub](https://opendatahub.io/)
* [Faust](https://github.com/robinhood/faust)

## Disclaimer

This project is currently designed for **Red Hat** internal usage only.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/akhil-rane/ludus/blob/master/LICENSE) file for details
