"""AI Provider Factory"""

import os
import logging
from app.ai.base import AIProvider
from app.ai.fallback import FallbackProvider

logger = logging.getLogger(__name__)


def get_ai_provider() -> AIProvider:
    """
    Factory function to get the appropriate AI provider based on environment configuration.
    
    Environment variables:
        AI_PROVIDER: openai | deepseek | local | fallback (default: fallback)
        AI_API_KEY: API key for the provider (optional)
        AI_MODEL: Model name (default: gpt-3.5-turbo)
    
    Returns:
        AIProvider instance
    """
    provider_name = os.getenv("AI_PROVIDER", "fallback").lower()
    api_key = os.getenv("AI_API_KEY")
    model = os.getenv("AI_MODEL", "gpt-3.5-turbo")
    
    # If no API key, use fallback
    if not api_key and provider_name != "fallback":
        logger.warning(f"No AI_API_KEY provided for provider '{provider_name}', using fallback")
        return FallbackProvider()
    
    # Return appropriate provider
    if provider_name == "openai" and api_key:
        try:
            from app.ai.openai_provider import OpenAIProvider
            logger.info(f"Using OpenAI provider with model: {model}")
            return OpenAIProvider(api_key, model)
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI provider: {e}, using fallback")
            return FallbackProvider()
    
    elif provider_name == "deepseek" and api_key:
        try:
            from app.ai.deepseek_provider import DeepSeekProvider
            logger.info(f"Using DeepSeek provider with model: {model}")
            return DeepSeekProvider(api_key, model)
        except Exception as e:
            logger.error(f"Failed to initialize DeepSeek provider: {e}, using fallback")
            return FallbackProvider()
    
    elif provider_name == "local":
        try:
            from app.ai.local_provider import LocalProvider
            logger.info(f"Using Local provider with model: {model}")
            return LocalProvider(model)
        except Exception as e:
            logger.error(f"Failed to initialize Local provider: {e}, using fallback")
            return FallbackProvider()
    
    else:
        logger.info("Using fallback rule-based provider")
        return FallbackProvider()


# Global provider instance
_provider_instance = None


def get_provider_instance() -> AIProvider:
    """Get or create singleton provider instance"""
    global _provider_instance
    if _provider_instance is None:
        _provider_instance = get_ai_provider()
    return _provider_instance
