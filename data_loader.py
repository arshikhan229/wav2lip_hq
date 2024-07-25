# data/data_loader.py
from google.colab import drive
drive.mount('/content/drive')

def copy_files():
    !cp /content/drive/MyDrive/wav2lip_gan.pth /content/wav2lip-hq/checkpoints/
