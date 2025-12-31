from imgprocalgs.algorithms.base import BaseImageAlgorithm
from imgprocalgs.genai.client import GenAIClient
import cv2


class GenAIImageEnhancer(BaseImageAlgorithm):
    """
    GenAI-based image enhancement algorithm.
    Uses a mock GenAI client to simulate enhancement.
    """

    def __init__(self, image_path: str, prompt: str | None = None):
        super().__init__(image_path)
        self.prompt = prompt
        self.client = GenAIClient(mode="mock")

    def process(self):
        # Load image using base functionality
        self.load_image()

        # Call GenAI client (mock enhancement)
        enhanced = self.client.enhance_image(
            self.image,
            prompt=self.prompt
        )

        self.result = enhanced
