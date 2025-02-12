import torch
import lpips
import os
from PIL import Image
from torchvision import transforms

# LPIPS 모델 불러오기
lpips_model = lpips.LPIPS(net='alex')  # 'alex', 'vgg', or 'squeeze' 모델 선택 가능

# 이미지 경로
source_folder = r"C:\jsj\MMC\FirstExam\MiniProject\pytorch-CycleGAN-and-pix2pix\results\cyclegan_exp_rain2shine_8batch\test_20\images"

# 이미지 불러오기 및 전처리 함수
def load_image(image_path):
    image = Image.open(image_path).convert('RGB')  # 이미지를 RGB로 변환
    preprocess = transforms.Compose([
        transforms.Resize((256, 256)),  # LPIPS 모델 입력 사이즈에 맞게 리사이즈 (필요시 조정)
        transforms.ToTensor(),  # 텐서로 변환
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # -1~1로 정규화
    ])
    image = preprocess(image).unsqueeze(0)  # 배치 차원 추가
    return image

# 파일 목록 불러오기
files = sorted(os.listdir(source_folder))

# LPIPS 점수 리스트
lpips_scores = []

# 6개씩 묶어서 비교
for i in range(0, len(files), 6):
    group = files[i:i+6]

    # 마지막 그룹이 6개 미만이면 경고 출력 후 종료
    if len(group) < 6:
        print("마지막 그룹에 이미지가 부족합니다:", group)
        break

    # 두 번째 fake 이미지와 네 번째 real 이미지 경로 설정
    fake_image_path = os.path.join(source_folder, group[1])  # 두 번째 fake 이미지
    real_image_path = os.path.join(source_folder, group[3])  # 네 번째 real 이미지

    # 이미지 불러오기
    fake_image = load_image(fake_image_path)
    real_image = load_image(real_image_path)

    # LPIPS 계산
    with torch.no_grad():  # 그래디언트 계산을 하지 않도록 설정
        lpips_score = lpips_model(fake_image, real_image)  # 두 이미지의 LPIPS 점수 계산
        lpips_scores.append(lpips_score.item())  # LPIPS 점수 리스트에 추가

# 평균 LPIPS 점수 계산
average_lpips_score = sum(lpips_scores) / len(lpips_scores) if lpips_scores else 0

print(f"Average LPIPS score: {average_lpips_score}")
