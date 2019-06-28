badges = {
    'first_pull': {
        'description': 'first pull request merged',
        'event_type': 'pull_request',
        'criteria': {
            'type': 'count',
            'value': 1
        },
        'image_file': None
    },
    'pull_master' : {
        'description': '10 pull requests merged',
        'event_type': 'pull_request',
        'criteria': {
            'type': 'count',
            'value': 10
        },
        'image_file': None
    },
    'first_issue': {
        'description': 'awarded for creating first issue',
        'event_type': 'issue',
        'criteria': {
            'type': 'count',
            'value': 1
        },
        'image_file': None
    },
    'issue_finder': {
        'description': 'awarded for creating 5 issues',
        'event_type': 'issue',
        'criteria': {
            'type': 'count',
            'value': 5
        },
        'image_file': None
    },
    'first_comment': {
        'description': 'awarded for first comment',
        'event_type': 'comment',
        'criteria': {
            'type': 'count',
            'value': 1
        },
        'image_file': None
    },
    'team_player': {
        'description': 'awarded for 5 comments',
        'event_type': 'comment',
        'criteria': {
            'type': 'count',
            'value': 5
        },
        'image_file': None
    },
    'homerun': {
        'description': 'awarded for opening issue, creating pull request, closing issue',
        'event_type': 'issue_closed',
        'criteria': {
            'type': 'match',
            'field': 'raw_github.issue.number',
            'matching_events': [
                {
                    'event_type': 'pull_request',
                    'field': 'issue_closes'
                },
                {
                    'event_type': 'issue',
                    'field': 'raw_github.issue.number'
                }
            ]
        },
        'image_file': None
    }
}
