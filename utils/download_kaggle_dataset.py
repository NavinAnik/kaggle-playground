import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_dataset(dataset_slug, download_path="datasets", unzip=True):
    os.makedirs(download_path, exist_ok=True)
    api = KaggleApi()
    api.authenticate()

    print(f"Downloading dataset: {dataset_slug}")
    api.dataset_download_files(dataset_slug, path=download_path, unzip=False)

    zip_path = os.path.join(download_path, dataset_slug.split('/')[-1] + '.zip')
    if unzip and os.path.exists(zip_path):
        print("Unzipping files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(download_path)
        os.remove(zip_path)

    print(f"Dataset downloaded to: {download_path}")

def download_kaggle_competition(competition_slug, download_path="datasets", unzip=True):
    import os
    import zipfile
    from kaggle.api.kaggle_api_extended import KaggleApi

    os.makedirs(download_path, exist_ok=True)
    api = KaggleApi()
    api.authenticate()

    print(f"Downloading competition data: {competition_slug}")
    api.competition_download_files(competition_slug, path=download_path)

    zip_path = os.path.join(download_path, competition_slug + '.zip')
    if unzip and os.path.exists(zip_path):
        print("Unzipping files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(download_path)
        os.remove(zip_path)

    print(f"Competition data downloaded to: {download_path}")
    return download_path
