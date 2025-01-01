import kagglehub
import shutil
import os

current_location = os.getcwd()
datasets_location = r'C:\Users\nijaa\.cache\kagglehub\datasets'

def load_dataset(location):
    # Download latest version
    path = kagglehub.dataset_download(location)
    print("Path to dataset files:", path)

    for filename in os.listdir(path):
        source_file = os.path.join(path, filename)

        # Only copy files (skip directories)
        if os.path.isfile(source_file):
            shutil.copy(source_file, current_location)
            print(f"Copied: {filename}")


if __name__ == '__main__':
    load_dataset("abdulmalik1518/the-ultimate-cars-dataset-2024")