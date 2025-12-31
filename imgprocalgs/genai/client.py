"""
GenAI client abstraction.

This client currently runs in MOCK mode to avoid paid API dependencies.
The structure is intentionally designed so a real GenAI API (OpenAI, HF, etc.)
can be plugged in later with minimal changes.
"""

import cv2
import numpy as np


class GenAIClient:
    def __init__(self, mode: str = "mock"):
        """
        :param mode: 'mock' or 'real'
        """
        self.mode = mode

    def enhance_image(self, image, prompt: str | None = None):
        """
        Mock image enhancement.
        Uses simple OpenCV operations to simulate enhancement.
        """
        if self.mode == "mock":
            # Simple enhancement: sharpen + slight contrast boost
            kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])
            enhanced = cv2.filter2D(image, -1, kernel)
            return enhanced

        raise NotImplementedError("Real GenAI mode not implemented")

    def convert_to_ghibli(self, image, prompt: str | None = None):
        """
        Mock Ghibli-style conversion.
        Uses color smoothing + warm tone to simulate a stylized look.
        """
        if self.mode == "mock":
            # Smooth colors
            stylized = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

            # Add warm tone
            stylized[:, :, 2] = cv2.add(stylized[:, :, 2], 20)
            stylized[:, :, 1] = cv2.add(stylized[:, :, 1], 10)

            return stylized

        raise NotImplementedError("Real GenAI mode not implemented")
