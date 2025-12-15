from flask import Flask, request, abort

from linebot.v3.webhook import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

app = Flask(__name__)

configuration = Configuration(
    access_token='60Es2r/q/CI9hW145TiwMAunEPkmhVE40R0Ca9fN5Smy9mhsfFZOKSdkiT1nRtt4TWgz1WqwY2CuhMU8SnzuLkHW/4HOVAETq0+LiB9cPEzS84Z1hs5oxOLdHlZQn3p1Ip3kzCoYDpwBx5QUgC17agdB04t89/1O/w1cDnyilFU='
)

handler = WebhookHandler('c461048f83f6faacd57cf5de7eb0101b')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers.get('X-Line-Signature')
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )


if __name__ == "__main__":
    app.run(port=5000)
