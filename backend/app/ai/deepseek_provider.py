"""DeepSeek AI provider (placeholder)"""

from app.ai.openai_provider import OpenAIProvider


class DeepSeekProvider(OpenAIProvider):
    """
    DeepSeek provider - uses OpenAI-compatible API.
    
    DeepSeek API is compatible with OpenAI's interface.
    """
    
    def __init__(self, api_key: str, model: str = "deepseek-chat"):
        super().__init__(api_key, model)
        # Override base URL for DeepSeek
        from openai import AsyncOpenAI
        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com/v1"
        )
