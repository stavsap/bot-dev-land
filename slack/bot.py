import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import logging
logging.basicConfig(level=logging.DEBUG)
# Initialize the Bolt app with your Bot User OAuth Access Token
# Initialize your app with your bot token and signing secret
token = os.environ.get("SLACK_BOT_TOKEN")
app_token = os.environ.get("SLACK_APP_TOKEN")
app = App(
    token=token,
    # signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    try:
        client.views_publish(
            user_id=event["user"],
            view={
                "type": "home",
                "callback_id": "home_view",
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Welcome to your _App's Home tab_* :tada:"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "This button won't do much for now, but you can set up a listener for it using the `actions()` method and passing its unique `action_id`."
                        }
                    }
                ]
            }
        )
    except Exception as e:
        logger.error(f"Error updating Home tab: {e}")

@app.message("hello")
def respond_to_hello(ack, message, say):
    # Acknowledge the message first
    ack()
    # Respond to the message with a predefined text
    say("Hello! How can I assist you today?")

# Start the app
if __name__ == "__main__":
    handler = SocketModeHandler(app=app, app_token=app_token)
    handler.start()
