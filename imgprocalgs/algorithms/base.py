from abc import ABC, abstractmethod
import cv2
import os


class BaseImageAlgorithm(ABC):
    """
    Abstract base class for all image processing algorithms
    Handles comon image loading and saving logic.
    """

    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image = None
        self.result = None

    def load_image(self):
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(f"Image not found: {self.image_path}")

        self.image = cv2.imread(self.image_path)
        if self.image is None:
            raise ValueError("Unable to load image")

    @abstractmethod
    def process(self):
        """
        Each algorithm must implement this method.
        """
        pass

    def save(self, output_path: str):
        if self.result is None:
            raise ValueError("No result generated")

        cv2.imwrite(output_path, self.result)
