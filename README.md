# 🌿 AgroScan
## 🧠 Model Training

The model training implementation is provided in the Jupyter Notebook:

**`AgroScan_AI/ml_model/notebooks/train_model_torch.ipynb`**

This notebook contains the training workflow for the AgroScan deep learning models, including **Swin Transformer Tiny** and **ConvNeXt Tiny**, along with model evaluation and performance analysis.

Open the notebook to explore the training process, model implementation, and experimental results.


------------------------------------------------------------------------
# 📊 Dataset

Name: Plant Disease Dataset

Source: Kaggle

Dataset link: https://www.kaggle.com/datasets/emmarex/plantdisease

The original dataset is approximately 660 MB in size, which exceeds GitHub's standard file upload limit. Therefore, instead of uploading the dataset directly to this repository, the publicly available Kaggle dataset link has been provided for download.
------------------------------------------------------------------------



**AI-Powered Plant Disease Detection Platform **

AgroScan is a deep learning-based plant disease detection platform
designed to assist farmers and researchers with crop diagnosis. It
combines a React frontend, a Python inference backend. Its plant disease classification approach uses two
pretrained models---**Swin Transformer Tiny** and **ConvNeXt
Tiny**---trained separately, with their predicted class probabilities
combined using a soft-voting ensemble.

The project also explores field-aware data augmentation and the
challenge of generalizing from controlled leaf images to real-world
field photographs.

------------------------------------------------------------------------

# ✨ Features

-   🌱 Plant disease classification from uploaded leaf images
-   🧠 Two pretrained deep-learning architectures: Swin Transformer Tiny
    and ConvNeXt Tiny
-   🤝 Soft-voting ensemble that combines probability outputs from both
    models
-   📊 Prediction confidence and class-probability visualization, where
    supported by the frontend
-   🖼️ Image upload with preview
-   🎨 Responsive frontend using React and Bootstrap
-   ⚡ Python-based inference pipeline
-   🔍 Evaluation using accuracy, precision, recall, F1-score, and
    confusion matrices
-   🌾 Field-aware augmentation experiments targeting lighting changes,
    blur, noise, viewpoint variation, and partial occlusion

------------------------------------------------------------------------


Dataset

# 📸 Screenshots

## 🌿 User Interface


<img width="1018" height="696" alt="Screenshot 2026-10-27 120613" src="https://github.com/user-attachments/assets/7dc0ebc5-a339-4934-84cc-d1e6c16dec31" />


------------------------------------------------------------------------

## 🔍 Disease Detection Results

<img width="812" height="1032" alt="Screenshot 2026-10-27 120756" src="https://github.com/user-attachments/assets/1be8d79f-5520-4d99-af2e-062a02fed5c9" />


------------------------------------------------------------------------

# 🏗️ System Architecture

### Architecture Overview

-   **Frontend:** React application for uploading leaf images and
    displaying predictions.
-   **Preprocessing:** Convert images to RGB, resize to `224 × 224`, and
    normalize according to the pretrained model requirements.
-   **Swin Transformer Tiny:** Learns hierarchical image representations
    using shifted-window self-attention.
-   **ConvNeXt Tiny:** Learns complementary visual features through
    hierarchical convolutional processing.
-   **Soft-voting ensemble:** Averages the probability vectors produced
    by the two independently trained models.
-   **Inference backend:** Python-based model inference, packaged for
    deployment where configured.

------------------------------------------------------------------------



