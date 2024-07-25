# main.py
from data.data_loader import copy_files
from models.model_loader import download_weights
from scripts.finetune import clone_repo, install_dependencies, download_weights

def main():
    clone_repo()
    install_dependencies()
    copy_files()
    download_weights()
    print("Setup complete. Ready for fine-tuning.")

if __name__ == "__main__":
    main()
