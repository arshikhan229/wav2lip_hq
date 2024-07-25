# models/model_loader.py
import gdown

urls = {
    "wav2lip_gan.pth": "10Iu05Modfti3pDbxCFPnofmfVlbkvrCm",
    "face_segmentation.pth": "154JgKpzCPW82qINcVieuPH3fZ2e0P812",
    "esrgan_yunying.pth": "1aB-jqBikcZPJnFrJXWUEpvF2RFCuerSe",
    "pretrained.state": "1_MGeOLdARWHylC1PCU2p5_FQztD4Bo7B"
}

for name, id in urls.items():
    url = f"https://drive.google.com/uc?id={id}"
    output = f"checkpoints/{name}"
    gdown.download(url, output, quiet=False)
    print(f"Loaded {name}")
