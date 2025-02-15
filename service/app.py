import sys
import os
import torch
from flask import Flask, render_template, request, send_file
from torchvision import transforms
from PIL import Image
from io import BytesIO

# 경로 추가 (models 폴더가 service 폴더 밖에 있을 경우)
sys.path.append('C:/jsj/MMC/FirstExam/MiniProject/pytorch-CycleGAN-and-pix2pix')

# 모델 불러오기 (A-to-B 변환용 Generator)
# networks.py 파일을 models 폴더에서 불러오기
from models import networks

# ResnetGenerator 불러오기
# norm을 norm_layer로 변경, n_blocks를 9로 설정
model = networks.ResnetGenerator(input_nc=3, output_nc=3, ngf=64, norm_layer=torch.nn.InstanceNorm2d, use_dropout=False, n_blocks=9)

# 가중치 파일 경로
model_path = 'C:/jsj/MMC/FirstExam/MiniProject/pytorch-CycleGAN-and-pix2pix/checkpoints/cyclegan_exp_sketches_bch/latest_net_G_A.pth'

# 모델에 가중치 로드
model.load_state_dict(torch.load(model_path))
model.eval()  # 모델을 평가 모드로 설정

# Flask 애플리케이션 생성
app = Flask(__name__)

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 이미지 업로드 및 모델 예측
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    # 파일 처리
    image = Image.open(file)

    # 이미지 전처리 없이 그대로 사용 (정규화하지 않음)
    image = transforms.ToTensor()(image).unsqueeze(0)  # 모델 입력에 맞게 차원 추가

    # 모델 예측 (A-to-B 변환)
    with torch.no_grad():
        output = model(image)

    # 출력 이미지 후처리: [-1, 1] -> [0, 1]
    output_image = output.squeeze().cpu().detach()
    output_image = (output_image + 1) / 2  # [-1, 1] -> [0, 1]

    # [0, 1] 범위를 [0, 255]로 변환
    output_image = output_image * 255

    # 이미지를 PIL 이미지로 변환
    output_image = transforms.ToPILImage()(output_image.byte())

    # 이미지를 메모리 내에서 반환
    img_byte_arr = BytesIO()
    output_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    return send_file(img_byte_arr, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)