"""Base classes and interfaces for TIR AI SDK"""

from abc import ABC, abstractmethod
from typing import Tuple, List


class BaseAISDK(ABC):
    """Base class for all AI SDK implementations"""

    @abstractmethod
    def get_response(self, text: str, model: str) -> Tuple[str, float]:
        """Get response from AI model

        Args:
            text: Input text to send to the model
            model: Name of the model to use

        Returns:
            Tuple of (response text, time taken in seconds)

        Raises:
            NotImplementedError: When the method is not implemented by a subclass
        """
        pass

    @staticmethod
    def list_models() -> List[str]:
        """List all available models

        Returns:
            List of model names supported by the SDK
        """
        return [
            'grok-2-latest',
            'deepseek-reasoner',
            'azure-o3-mini',
            'gpt-4o'
        ]
