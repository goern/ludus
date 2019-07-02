from validators import pull_request_validator
from validators import issue_validator


event_configuration = {
    "pull_request" : {
        "validator" : pull_request_validator.schema,
        "formatter" : "formatters/pull_request_formmatter"
    },

    "issue" : {
        "validator" : issue_validator.schema,
        "formatter" : "formatters/issue_formmatter"
    }
}