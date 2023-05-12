from ultralytics import YOLO
import yaml
from typing import List


# Load a model
model = YOLO("yolov8s.pt")  # load a pretrained model (recommended for training)

PREDICT_LABELS_PATH = "/Users/abdibrokhim/VisualStudioCode/runs/detect/predict/labels/macbook.txt"

COCO8_PATH = "/Users/abdibrokhim/VisualStudioCode/Med-Announce/productDetection/env/lib/python3.11/site-packages/ultralytics/datasets/coco8.yaml"


def predict(image: str) -> List[str]:
    model.predict(image, save=True, save_txt=True)

    return get_label_names()


def get_label_names() -> List[str]:
    file_name = COCO8_PATH

    # Load label names from YAML file
    try:
        with open(file_name, "r") as stream:
            names = yaml.safe_load(stream)["names"]
    except Exception as e:
        print(e)
        names = []

    # Load label lines from prediction file
    label_lines = open(PREDICT_LABELS_PATH, "r").readlines()

    labels = []

    # Get label names from label lines
    for line in label_lines:
        ind = int(line.split()[0])
        print(ind, names[ind])
        labels.append(names[ind])

    label_lines.close()

    return labels


if __name__ == "__main__":
    img = "data/train/macbook.jpg"
    print(predict(img))
