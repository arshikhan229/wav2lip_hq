# scripts/finetune.py
import subprocess

def clone_repo():
    subprocess.run(["git", "clone", "https://github.com/Markfryazino/wav2lip-hq.git"])

def install_dependencies():
    subprocess.run(["pip3", "install", "gdown"])
    subprocess.run(["pip3", "install", "-r", "requirements.txt"])

def download_weights():
    subprocess.run(["wget", "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth", "-O", "face_detection/detection/sfd/s3fd.pth"])
