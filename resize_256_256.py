
import os
from PIL import Image

# 이미지가 저장된 원본 폴더 경로
input_folder = r'C:\jsj\MMC\FirstExam\MiniProject\DownloadData\sketches\cyclegan\trainB'

# 리사이즈된 이미지를 저장할 새로운 폴더 경로
output_folder = r'C:\jsj\MMC\FirstExam\MiniProject\DownloadData\sketches\cyclegan\trainBB'

# output_folder가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# input_folder 내의 모든 파일에 대해 리사이즈 후 저장
for filename in os.listdir(input_folder):
    # 파일 경로 만들기
    img_path = os.path.join(input_folder, filename)

    # 이미지 파일만 처리
    if os.path.isfile(img_path):
        try:
            # 이미지 열기
            img = Image.open(img_path)

            # 256x256으로 리사이즈
            img_resized = img.resize((256, 256))

            # 리사이즈된 이미지 저장
            output_path = os.path.join(output_folder, filename)
            img_resized.save(output_path)
            print(f"Saved resized image: {output_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

