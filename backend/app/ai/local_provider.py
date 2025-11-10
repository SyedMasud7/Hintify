"""Local model AI provider (placeholder)"""

from app.ai.fallback import FallbackProvider


class LocalProvider(FallbackProvider):
    """
    Local model provider - placeholder for local LLM inference.
    
    This would integrate with local models like Llama, Mistral, etc.
    For now, falls back to rule-based provider.
    """
    
    def __init__(self, model: str):
        super().__init__()
        self.model = model
        # TODO: Implement local model loading and inference
