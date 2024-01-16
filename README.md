# Motorbike-and-Number-Plate-Detection

This project is focused on detecting both motorbikes and their number plates using TensorFlow and Docker. The primary goal is to develop a system that not only identifies motorbikes in images but also extracts and recognizes the license numbers from their number plates. The project uses a pre-trained Faster R-CNN (Region-based Convolutional Neural Network) model for motorbike detection.

## Pre-trained Model
A pre-trained Faster R-CNN model has been utilized for motorbike detection. The final model is saved in the repository for easy access and implementation.

## License Number Recognition (In Progress)
The project is actively working on developing license number recognition from the detected number plates. This feature aims to enhance the functionality of the system, making it more comprehensive and practical for various applications.

## Results

### Input Images

![Image 1](https://github.com/Subham-4/Motorbike-and-Number-Plate-Detection/assets/84079854/11c6fb57-d79e-43c5-ab0e-cb64a0bc5f3f)

![Image 2](https://github.com/Subham-4/Motorbike-and-Number-Plate-Detection/assets/84079854/c04e7ea6-8b9a-40ae-934a-d47353a64cf0)

![Image 3](https://github.com/Subham-4/Motorbike-and-Number-Plate-Detection/assets/84079854/89184b53-aa65-4272-97f7-7145de58fc27)

### Output Images

![Output 1](https://github.com/Subham-4/Motorbike-and-Number-Plate-Detection/assets/84079854/469f73ff-9254-4d73-97f1-37f4055224aa)

![Output 2](https://github.com/Subham-4/Motorbike-and-Number-Plate-Detection/assets/84079854/1b562693-b1f2-4360-b70b-59700048838b)

![Output 3](https://github.com/Subham-4/Motorbike-and-Number-Plate-Detection/assets/84079854/193731d0-5136-45b9-85d8-0f7eb29c4534)

## Usage

To use the system, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Subham-4/Motorbike-and-Number-Plate-Detection.git
   ```

2. Run the Docker container:

   ```bash
   docker build -t motorbike_detection .
   docker run -it motorbike_detection
   ```

   This will set up the environment and dependencies required for motorbike and number plate detection.

## Acknowledgments

The project uses a pre-trained model and is grateful for the contributions of the machine learning community. Credits to the authors and contributors of the Faster R-CNN model used in this project.
