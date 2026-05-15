# 🌿 AgroScan

**AI-Powered Plant Disease Detection Platform — Cloud-Native and Scalable**

AgroScan is a deep learning-based plant disease detection platform designed to assist farmers and researchers with fast and reliable crop diagnosis. The platform combines a modern React frontend, serverless Python backend, ONNX-based inference pipeline, and AWS cloud infrastructure for scalable real-time disease prediction.

---

# 📑 Table of Contents

1. [🚀 Live Demo](#-live-demo)
2. [✨ Features](#-features)
3. [📸 Screenshots](#-screenshots)
4. [🏗️ System Architecture](#️-system-architecture)
5. [🛠️ Tech Stack](#️-tech-stack)
6. [📂 Project Structure](#-project-structure)
7. [⚙️ Setup & Deployment](#️-setup--deployment)
8. [🤖 Model Training & ONNX Conversion](#-model-training--onnx-conversion)
9. [🚧 Future Improvements](#-future-improvements)
10. [👨‍💻 Author](#author)

---

# 🚀 Live Demo

🔗 **[Try AgroScan](https://main.d3n8iyuxmo9pz7.amplifyapp.com/)**

---

# ✨ Features

- 🌱 AI-powered plant disease detection from uploaded crop images
- 🧠 Vision Transformer (ViT) based classification model
- 📊 Top-5 prediction confidence visualization
- ⚡ Serverless ONNX inference pipeline using AWS Lambda
- ☁️ Cloud-native deployment using AWS services
- 🖼️ Drag-and-drop image upload with real-time preview
- 🎨 Modern responsive frontend using React and Bootstrap
- 🐳 Dockerized backend deployment for scalability
- 🔍 Optimized inference using ONNX Runtime

---

# 📸 Screenshots

## 🌿 User Interface

<img width="1918" height="1012" alt="UI Screenshot" src="https://github.com/user-attachments/assets/aaa36c1f-b36c-463e-850b-3161cd32ccc0" />

---

## 🔍 Disease Detection Results

<img width="1913" height="1008" alt="Prediction Screenshot" src="https://github.com/user-attachments/assets/857c7f4b-b56c-4313-9f85-3d4339767b57" />

---

## 📊 Model Accuracy Curve

<img width="1263" height="682" alt="Accuracy Curve" src="https://github.com/user-attachments/assets/23a448fb-d7ab-4a5c-89e0-02dde545a1e6" />

---

# 🏗️ System Architecture

<img width="1024" height="1024" alt="Architecture Diagram" src="https://github.com/user-attachments/assets/216825b3-38f8-45cf-b48f-3c483e6b4c6b" />

### Architecture Overview

- React frontend hosted using AWS Amplify
- Image upload and prediction requests handled through AWS Lambda
- Dockerized ONNX inference pipeline for scalable deployment
- ONNX Runtime used for optimized AI inference
- Amazon ECR stores backend container images
- Modular cloud-native architecture enables scalability and reliability

---

# 🛠️ Tech Stack

| Layer | Technologies & Tools |
| :-- | :-- |
| **Frontend** | React.js, Vite, Bootstrap, JavaScript |
| **Backend** | Python, AWS Lambda, Docker |
| **Machine Learning** | PyTorch, timm, ONNX, ONNX Runtime, OpenCV |
| **Cloud & Deployment** | AWS Amplify, Amazon ECR, AWS Lambda |
| **Utilities** | NumPy, Pillow, REST APIs |

---

# 📂 Project Structure

```bash
AgroScan/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── config/
│   │   └── assets/
│   ├── public/
│   └── vite.config.js
│
├── ml_model/
│   ├── Dockerfile
│   ├── app_lambda.py
│   ├── requirements.txt
│   ├── save_as_onnx.py
│   ├── verify_onnx.py
│   └── notebooks/
│
├── README.md
└── .gitignore
```

---

# ⚙️ Setup & Deployment

## 1️⃣ Clone Repository

```bash
git clone https://github.com/PurushothamaReddyM/Agroscan.git
cd Agroscan
```

---

## 2️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Production Build

```bash
npm run build
```

Frontend deployment is configured using AWS Amplify.

---

## 3️⃣ Backend Setup

```bash
cd ml_model
pip install -r requirements.txt
```

---

## 4️⃣ Docker Build

```bash
docker build -t agroscan .
```

---

## 5️⃣ Deploy Backend to AWS Lambda

### Push Docker Image to Amazon ECR

```bash
aws ecr get-login-password | docker login --username AWS --password-stdin
docker push <your-ecr-url>/agroscan:latest
```

### Configure Deployment

- Deploy Docker container to AWS Lambda
- Configure Lambda function URL or API Gateway
- Monitor logs using AWS CloudWatch

---

# 🤖 Model Training & ONNX Conversion

The plant disease classification model was trained using PyTorch and converted to ONNX format for optimized cloud inference.

### ONNX Conversion

```bash
python save_as_onnx.py
```

### ONNX Verification

```bash
python verify_onnx.py
```

### Model Features

- ✅ Vision Transformer (`vit_tiny_patch16_224`)
- 🌱 38 plant disease classes
- ⚡ ONNX Runtime optimized inference
- ☁️ Serverless deployment ready

---

# 🚧 Future Improvements

- Multi-language support for farmers
- Treatment recommendation system
- Mobile application support
- Real-time camera disease detection
- Improved explainability using Grad-CAM
- Expanded crop and disease dataset

---

# Author

## M Purushothama Reddy

- B.Tech Computer Science Engineering Student
- AI/ML & Full Stack Development Enthusiast
- Interested in Cloud-Native AI Systems and Deployment Engineering

<p align="left">

<a href="mailto:reddypurushothama257@gmail.com" target="blank">
<img align="center" src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="email" height="40" width="40" />
</a>

<a href="https://www.linkedin.com/in/machupalli-purushothama-reddy-8544793b4/" target="blank">
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="linkedin" height="40" width="40" />
</a>

<a href="https://github.com/PurushothamaReddyM" target="blank">
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="github" height="40" width="40" />
</a>

</p>
