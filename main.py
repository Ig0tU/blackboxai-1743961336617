import os
from fastapi_poe import PoeBot, make_app, stream_request
from fastapi_poe.types import QueryRequest, PartialResponse, SettingsRequest, SettingsResponse
from typing import AsyncIterable

class MultiModelBot(PoeBot):
    async def get_response(self, request: QueryRequest) -> AsyncIterable[PartialResponse]:
        try:
            async for claude_msg in stream_request(
                request, "Claude-3.7-Sonnet", request.access_key
            ):
                yield PartialResponse(text=claude_msg.text + "\n")

            async for gemini_msg in stream_request(
                request, "Gemini-Pro", request.access_key
            ):
                yield PartialResponse(text=gemini_msg.text + "\n")
        except Exception as e:
            yield PartialResponse(text=f"Error: {str(e)}\n")

    async def get_settings(self, setting: SettingsRequest) -> SettingsResponse:
        return SettingsResponse(
            server_bot_dependencies={
                "Claude-3.7-Sonnet": 1,
                "Gemini-Pro": 1,
            },
            allow_attachments=True,
            introduction_message="Hi! I'm a multi-model bot that uses both Claude 3.7 Sonnet and Gemini Pro. Ask me anything!",
            context_clear_window_secs=600
        )

from dotenv import load_dotenv
load_dotenv()

bot_name = os.getenv("BOT_NAME")
access_key = os.getenv("ACCESS_KEY")

if not bot_name or not access_key:
    raise ValueError("BOT_NAME and ACCESS_KEY environment variables must be set")
from dotenv import load_dotenv
load_dotenv()

# Initialize the app using environment variables
bot_name = os.getenv("BOT_NAME")
access_key = os.getenv("ACCESS_KEY")

if not bot_name or not access_key:
    raise ValueError("BOT_NAME and ACCESS_KEY environment variables must be set")

app = make_app(
    MultiModelBot(),
    bot_name=bot_name,
    access_key=access_key
)
