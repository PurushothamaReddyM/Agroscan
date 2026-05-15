# 🌿 AgroScan

**AI-Powered Plant Disease Detection Platform — Cloud-Native, Scalable, and Production-Ready**

AgroScan is a deep learning-based plant disease detection platform designed to assist farmers and researchers with fast and reliable crop diagnosis. The platform combines a modern React frontend, FastAPI backend, and AWS serverless infrastructure for scalable real-time predictions.

---

# 📑 Table of Contents

1. [Live Demo](#-live-demo)
2. [Features](#-features)
3. [Screenshots](#-screenshots)
4. [Architecture](#-architecture)
5. [Tech Stack](#-tech-stack)
6. [Project Structure](#-project-structure)
7. [Setup & Deployment](#-setup--deployment)
8. [Model Training](#-model-training)
9. [Future Improvements](#-future-improvements)
10. [Author](#-author)


---

# 🚀 Live Demo

🔗 **[Try AgroScan](https://main.d3n8iyuxmo9pz7.amplifyapp.com/)**

---

# ✨ Features

- 🌱 Instant plant disease prediction from uploaded images
- 🧠 Deep learning model trained on 38+ crop disease classes
- ⚡ FastAPI backend deployed using AWS Lambda and Docker
- ☁️ Cloud-native serverless architecture with AWS services
- 🎨 Modern responsive frontend built with React and Tailwind CSS
- 🔄 Automated CI/CD workflows using GitHub Actions
- 📈 Optimized for scalability, performance, and reliability

---

# 📸 Screenshots

## 🌿 User Interface
<img width="1918" height="1012" alt="UI Screenshot" src="https://github.com/user-attachments/assets/aaa36c1f-b36c-463e-850b-3161cd32ccc0" />

## 🔍 Disease Detection Results
<img width="1913" height="1008" alt="Prediction Screenshot" src="https://github.com/user-attachments/assets/857c7f4b-b56c-4313-9f85-3d4339767b57" />

## 📊 Model Accuracy Curve
<img width="1263" height="682" alt="Accuracy Curve" src="https://github.com/user-attachments/assets/23a448fb-d7ab-4a5c-89e0-02dde545a1e6" />

---

# 🏗️ Architecture

<img width="1024" height="1024" alt="Architecture Diagram" src="https://github.com/user-attachments/assets/216825b3-38f8-45cf-b48f-3c483e6b4c6b" />

### Architecture Overview

- AWS Amplify hosts the frontend application
- API Gateway securely routes prediction requests
- AWS Lambda runs FastAPI inside Docker containers
- Amazon ECR stores backend container images
- Modular cloud-native architecture enables scalability and reliability

---

# 🛠️ Tech Stack

| Layer | Technologies & Tools |
| :-- | :-- |
| **Frontend** | React.js, Tailwind CSS, Vite, JavaScript, AWS Amplify |
| **Backend** | FastAPI, Python, Docker, AWS Lambda, AWS API Gateway |
| **Machine Learning** | TensorFlow, Keras, PyTorch, ONNX, OpenCV |
| **Cloud & DevOps** | AWS Amplify, Amazon ECR, GitHub Actions, Docker, CloudWatch |
| **Build Tools** | npm, ESLint, Vite |

---

# 📂 Project Structure

```bash
AgroScan/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── assets/
│   │   └── config/
│   ├── public/
│   └── vite.config.js
│
├── ml_model/
│   ├── Dockerfile
│   ├── app_lambda.py
│   ├── requirements.txt
│   ├── save_as_onnx.py
│   └── notebooks/
│
├── package.json
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

Frontend deployment is configured using AWS Amplify with automatic deployment from the GitHub main branch.

---

## 3️⃣ Backend Setup

```bash
cd ml_model
pip install -r requirements.txt
```

### Docker Build

```bash
docker build -t agroscan .
```

### Push Docker Image to Amazon ECR

```bash
aws ecr get-login-password | docker login --username AWS --password-stdin
docker push <your-ecr-url>/agroscan:latest
```

### Deploy Backend

- Deploy the Docker container to AWS Lambda
- Configure API Gateway for secure API routing
- Monitor logs using AWS CloudWatch

---

# 🤖 Model Training

The deep learning model was trained using TensorFlow/Keras with image augmentation and normalization techniques for improved generalization.

### Training Workflow

```bash
ml_model/notebooks/model_training_notebook.ipynb
```

### Model Performance

- ✅ 98%+ validation accuracy
- 🌱 38+ plant disease classes
- ⚡ Optimized inference pipeline for cloud deployment

---

# 🚧 Future Improvements

- Better handling for invalid image uploads
- CLI support for model retraining
- Enhanced UI feedback and confidence visualization
- Expanded troubleshooting and deployment documentation
- Multi-language support for farmers

---

# 👨‍💻 Author

### Purushothama Reddy M

Full Stack Developer • AI/ML Enthusiast • Cloud & Backend Development


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

---
