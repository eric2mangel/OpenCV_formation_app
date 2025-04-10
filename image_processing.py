import cv2
import numpy as np

def apply_blur(image, blur_radius):
    """Applique un flou gaussien à l'image."""
    blurred = cv2.GaussianBlur(image, (blur_radius * 2 + 1, blur_radius * 2 + 1), 0)
    return blurred

def apply_canny(image, threshold1, threshold2):
    """Applique la détection de bords Canny à l'image."""
    edges = cv2.Canny(image, threshold1, threshold2)
    return edges

# Vous ajouterez d'autres fonctions de traitement ici