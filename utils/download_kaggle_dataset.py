import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_dataset(dataset_slug, download_path="datasets", unzip=True):
    """
    Downloads a Kaggle dataset using the Kaggle API.

    Parameters:
    - dataset_slug (str): Dataset slug from Kaggle (e.g. 'zynicide/wine-reviews')
    - download_path (str): Local folder to store the dataset
    - unzip (bool): Whether to unzip the downloaded file
    """
    # Ensure the destination exists
    os.makedirs(download_path, exist_ok=True)

    # Initialize Kaggle API
    api = KaggleApi()
    api.authenticate()

    print(f"Downloading dataset: {dataset_slug}")
    api.dataset_download_files(dataset_slug, path=download_path, unzip=False)

    # Unzip if required
    zip_path = os.path.join(download_path, dataset_slug.split('/')[-1] + '.zip')
    if unzip and os.path.exists(zip_path):
        print("Unzipping files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(download_path)
        os.remove(zip_path)

    print(f"Dataset downloaded to: {download_path}")