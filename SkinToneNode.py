import cv2
import numpy as np

class SkinToneNode:
    def __init__(self):
        self.color = [255, 220, 200]  # 기본 피부톤 RGB
        self.intensity = 0.5  # 적용 강도

    def process(self, image):
        # 얼굴 영역 검출 (여기서는 간단히 전체 이미지로 가정)
        face_region = image.copy()
        
        # 색상 보정 마스크 생성
        color_layer = np.full(face_region.shape, self.color, dtype=np.uint8)
        
        # 피부톤 적용
        result = cv2.addWeighted(face_region, 1-self.intensity, color_layer, self.intensity, 0)
        
        return result

# ComfyUI 노드 시스템에 등록
NODE_CLASS_MAPPINGS = {
    "SkinToneNode": SkinToneNode
}