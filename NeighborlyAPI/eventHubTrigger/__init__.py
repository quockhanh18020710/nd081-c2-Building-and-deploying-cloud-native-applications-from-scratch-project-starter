import json
import logging
import azure.functions as func

def main(event: func.EventGridEvent):
    logging.info('Function triggered to process a message: %s', event.get_json())
    logging.info('  Event Time: %s', event.event_time)
    logging.info('  Event ID: %s', event.id)
    logging.info('  Event Type: %s', event.event_type)
    logging.info('  Event Subject: %s', event.subject)
    logging.info('  Event Topic: %s', event.topic)

    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
        'event_time': event.event_time.isoformat()
    })

    logging.info('Python EventGrid trigger processed an event: %s', result)
