"""
 * Copyright 2019 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

import os
import logging
import requests
from google.cloud import bigquery

BQ_CLIENT = bigquery.Client()
logging.getLogger().setLevel(logging.INFO)

VARIABLES = {
    "SLACK_WEBHOOK_URL": os.getenv("SLACK_WEBHOOK_URL"),
    "DATASET_NAME": os.getenv("DATASET_NAME"),
    "AUDIT_LOG_TABLE":  os.getenv("AUDIT_LOG_TABLE"),
    "TIME_COLUMN": os.getenv("TIME_COLUMN"),
    "ERROR_MESSAGE_COLUMN": os.getenv("ERROR_MESSAGE_COLUMN")
}
QUERY = """
WITH
  errors AS (
  SELECT
    {ERROR_MESSAGE_COLUMN} AS error_message,
    EXTRACT(HOUR FROM current_timestamp) as hr
  FROM
    {DATASET_NAME}.{AUDIT_LOG_TABLE}
  WHERE
    {ERROR_MESSAGE_COLUMN} IS NOT NULL
    AND EXTRACT(HOUR
    FROM
      current_timestamp) = EXTRACT(HOUR
    FROM
     {TIME_COLUMN}))
SELECT
  error_message as Error,
  hr,
  COUNT(*) as Count
FROM
  errors
GROUP BY
  1,2
""".format(**VARIABLES)

def query_for_errors(pubsub_event, pubsub_context):
    """
    Cloud Function to query audit logs for errors
    and send alerts to Slack Webhook
    """
    
    logging.info("Running: %s", QUERY)
    query_job = BQ_CLIENT.query(QUERY)

    if list(query_job):
        for row in list(query_job):
            text = ("Alert: Error {0}... has occurred {1} times"
                    "in the past hour - {2}:00 PST. "
                    "Please file a bug ticket to have").format(
                        (row["Error"][:500]),
                        str(row["Count"]),
                        str(row["hr"]))
            logging.info("Posting to Slack: %s", text)
            req = requests.post(url=VARIABLES['SLACK_WEBHOOK_URL'],
                                data=str({"text": text}))
            logging.info(req.text)

if __name__ == "__main__":
    query_for_errors(None, None)
