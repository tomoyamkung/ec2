import json
import logging
from datetime import date, datetime
from typing import Any, Dict, List, Optional

import boto3

from data import Instance
from execution_environment import Environment


def lambda_handler(event: dict[str, str], context: str) -> Dict[str, Any]:
    # { "env": "dev" }
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info(json.dumps(event))

    # if "challenge" in event:
    #     return event.get("challenge")

    _env: Optional[Environment] = Environment.get_by(event.get("env"))
    _filters = _env.to_filter if _env else {}

    response = boto3.client("ec2", region_name="ap-northeast-1").describe_instances(
        Filters=[_filters]
    )
    logger.info(json.dumps(response, cls=CustomJSONEncoder))

    instances: List[Instance] = []
    for _ele in response["Reservations"]:
        instances.extend([Instance(e) for e in _ele["Instances"]])

    response_body = "\n".join(
        [str(e) for e in sorted(instances, key=lambda instance: instance.name)]
    )
    logger.info(response_body)

    return {
        "statusCode": 200,
        "body": response_body,
    }


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, "__iter__"):
            return list(o)
        elif isinstance(o, (datetime, date)):
            return o.isoformat()
        else:
            return str(o)
