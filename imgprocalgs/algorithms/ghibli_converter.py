from imgprocalgs.algorithms.base import BaseImageAlgorithm
from imgprocalgs.genai.client import GenAIClient


class GhibliStyleConverter(BaseImageAlgorithm):
    """
    GenAI-based image to Studio Ghibli style converter.
    Uses a mock GenAI client to simulate artistic style transfer.
    """

    def __init__(self, image_path: str, prompt: str | None = None):
        super().__init__(image_path)
        self.prompt = prompt
        self.client = GenAIClient(mode="mock")

    def process(self):
        # Load image using base functionality
        self.load_image()

        # Call GenAI client (mock Ghibli-style conversion)
        stylized = self.client.convert_to_ghibli(
            self.image,
            prompt=self.prompt
        )

        self.result = stylized
