from flask import Flask, request, abort
from linebot.v3.webhook import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    Configuration, ApiClient, MessagingApi,
    ReplyMessageRequest, TextMessage
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent
import os

app = Flask(__name__)

configuration = Configuration(
    access_token=os.environ.get("60Es2r/q/CI9hW145TiwMAunEPkmhVE40R0Ca9fN5Smy9mhsfFZOKSdkiT1nRtt4TWgz1WqwY2CuhMU8SnzuLkHW/4HOVAETq0+LiB9cPEzS84Z1hs5oxOLdHlZQn3p1Ip3kzCoYDpwBx5QUgC17agdB04t89/1O/w1cDnyilFU=")
)
handler = WebhookHandler(os.environ.get("c461048f83f6faacd57cf5de7eb0101b"))


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers.get("X-Line-Signature")
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        MessagingApi(api_client).reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )


# ⚠️ gunicorn 會用到，但這段保留給本機測試
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
