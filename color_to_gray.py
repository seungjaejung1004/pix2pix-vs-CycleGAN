import cv2
import os

# 컬러사진 경로, 흑백화하고 저장할 경로 지정
color_image_path = r'C:\jsj\MMC\FirstExam\MiniProject\DownloadData\colorlization\pix2pix\trainB'
saved_gray_image_path = r'C:\jsj\MMC\FirstExam\MiniProject\DownloadData\colorlization\pix2pix\trainA'

# 저장할 주소 지정
os.makedirs(saved_gray_image_path, exist_ok=True)

# Process each image
for filename in os.listdir(color_image_path):
    # Construct full file paths
    input_file = os.path.join(color_image_path, filename)
    output_file = os.path.join(saved_gray_image_path, filename)

    # lower을 사용해 대소문자 구분 안함. jpg사진만 처리
    if filename.lower().endswith('.jpg'):
        try:
            # 컬러이미지 읽어옴
            color_image = cv2.imread(input_file)

            # 컬러 이미지를 흑백이미지로 변환
            gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

            # 흑백변환한 사진 저장
            cv2.imwrite(output_file, gray_image)
        except Exception as e:
            print(f"Error processing file {filename}: {e}")
