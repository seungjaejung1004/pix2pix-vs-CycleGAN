import sys
# 경로를 Python 경로에 추가합니다
sys.path.append('C:/jsj/MMC/FirstExam/MiniProject/pytorch-CycleGAN-and-pix2pix')

# sys.path에 경로가 제대로 추가되었는지 확인
print(sys.path)

from models.cycle_gan_model import CycleGANModel
from options.train_options import TrainOptions