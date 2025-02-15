## ✅ Pix2Pix와 CycleGAN 비교 프로젝트


## 🛠️ 개발도구
<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="40"> <img src="https://upload.wikimedia.org/wikipedia/commons/1/10/PyTorch_logo_icon.svg" width="40">


## 📝 실험목적
Paired dataset 기반으로 학습하는 모델인 Pix2Pix와 Unpaired dataset 기반으로 학습하는 CycleGAN을 활용한 여러가지 실험을 통해 각 모델의 장점과 단점을 분석하는 것을 목표로 실행하였습니다. 이번 연구에서 진행한 실험은 3가지로 다음과 같습니다.
- Colorization
- Cartoonization
- Denoising

실험 이후 객관적 평가를 위해 인간의 시각 시스템을 모방하여 이미지간의 지각적인 유사도를 평가하는 지표인 LPIPS 평가지표를 사용하여 평가하였습니다.

## 📊 실험결과
### \<Colorization\>
![image](https://github.com/user-attachments/assets/8a34d0a4-a650-49a9-810f-2898af74ccd5)

### \<Cartoonization\>
![image](https://github.com/user-attachments/assets/f37b7403-9e6c-4100-9279-4d1c78ef04d5)

### \<Denoising\>
![image](https://github.com/user-attachments/assets/bdaef6a7-7d35-47e0-a66a-c5184451fc03)

### \<LPIPS Score\>
![image](https://github.com/user-attachments/assets/b96e6919-491e-4ed1-9553-8b4cd0c94512)


## 📌 결론
- 모든 실험에서 Pix2Pix가 CycleGAN보다 우수한 성능을 보여주었다. CycleGAN과는 달리 Pix2Pix에는 실제정답과 비교하는 L1 Loss가 손실함수로 있기 때문에 당연한 결과였다.  하지만 실제로는 Paired dataset이 없는 경우가 대부분인데 CycleGAN은 Paired dataset이 존재하지 않을때 Ubpaired dataset으로도 Pix2Pix 못지 않은 성능을 낸 부분에서 의미가 있다

## 🌐 응용서비스
![캡처](https://github.com/user-attachments/assets/32c4873c-ee58-4e3d-9c21-67f987456729)
![a](https://github.com/user-attachments/assets/a6babda6-4bc1-4d74-b47e-1cc6c46e0c3a)

