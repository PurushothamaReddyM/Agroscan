
# AgroScan AI

**AI-Powered Plant Disease Detection — Serverless, Cloud-Native, Production-Ready**

AgroScan AI leverages deep learning and AWS serverless architecture for instant crop disease diagnosis. Farmers and researchers get fast, reliable results through a React frontend, a Python Lambda-style backend, and automated cloud deployment.

***

## Table of Contents

1. [Live Demo](#live-demo)
2. [Features](#features)
3. [Screenshots](#screenshots)
4. [Architecture](#architecture)
5. [Tech Stack](#tech-stack)
6. [Project Structure](#project-structure)
7. [Local Development](#local-development)
8. [Model Training](#model-training)
9. [Planned Improvements](#planned-improvements)
10. [Author](#author)
11. [License](#license)

***

## Live Demo

- **[Try AgroScan AI](https://main.d3n8iyuxmo9pz7.amplifyapp.com/)**

***

## Features

- Instant crop disease diagnosis from images
- 38+ supported crop-disease classes (maize, tomato, apple, grape, etc.)
- Serverless backend (Python Lambda handler on AWS Lambda using Docker/ECR, API Gateway)
- Modern, responsive React + Tailwind CSS frontend (AWS Amplify)
- Easy retraining, modular infrastructure, seamless CI/CD via GitHub Actions
- Optimized for scalability and reliability

***

## Screenshots

**User Interface**
<img width="1918" height="1012" alt="Screenshot 2025-10-01 232836" src="https://github.com/user-attachments/assets/aaa36c1f-b36c-463e-850b-3161cd32ccc0" />

**Detection Results**
<img width="1913" height="1008" alt="Screenshot 2025-10-01 233020" src="https://github.com/user-attachments/assets/857c7f4b-b56c-4313-9f85-3d4339767b57" />

**Accuracy Curve**
<img width="1263" height="682" alt="Screenshot 2025-10-01 234333" src="https://github.com/user-attachments/assets/23a448fb-d7ab-4a5c-89e0-02dde545a1e6" />

***

## Architecture

<img width="1024" height="1024" alt="Gemini_Generated_Image_7q1le07q1le07q1l" src="https://github.com/user-attachments/assets/216825b3-38f8-45cf-b48f-3c483e6b4c6b" />
*AWS Amplify for frontend, API Gateway for secure routing, Lambda (ECR/Docker) running the Python backend, and modular, cloud-native design.*

***

## Tech Stack

| Layer | Technologies \& Tools |
| :-- | :-- |
| **Frontend** | React.js, Tailwind CSS, Vite, JavaScript, AWS Amplify |
| **Frontend Build** | Vite, npm, ESLint |
| **Backend** | Python Lambda handler, Docker, AWS Lambda, AWS API Gateway, AWS ECR |
| **ML Model** | TensorFlow, Keras, PyTorch, ONNX, OpenCV |
| **Infra / CI/CD** | AWS Amplify, Docker, GitHub Actions, Vercel (testing), AWS CloudWatch |


***

## Project Structure

```
AgroScan_AI/
├── .gitignore
├── README.md
├── package-lock.json
├── package.json
├── frontend/
│   ├── .gitignore
│   ├── README.md
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── vercel.json
│   ├── vite.config.js
│   ├── public/
│   │   └── vite.svg
│   └── src/
│       ├── App.css
│       ├── App.jsx
│       ├── index.css
│       ├── main.jsx
│       ├── assets/
│       │   └── react.svg
│       ├── components/
│       │   ├── ImageUploader.jsx
│       │   ├── Loader.jsx
│       │   ├── PlantDiseasePredictor.jsx
│       │   ├── PlantSelector.jsx
│       │   ├── PredictionResult.jsx
│       │   └── TopKModal.jsx
│       └── config/
│           └── plants.js
├── ml_model/
│   ├── Dockerfile
│   ├── app_lambda.py
│   ├── check_model.py
│   ├── check_onnx.py
│   ├── require
│   ├── requirements-min.txt
│   ├── requirements.txt
│   ├── save_as_onnx.py
│   ├── temp.jpg
│   └── notebooks/
│       └── convert_to_tfjs.py
```


***

## Local Development

### Prerequisites

- Node.js 18+ and npm
- Python 3.10 x64
- Git

The backend depends on `onnxruntime`, so use Python 3.10 on Windows for the local backend environment.

### 1. Clone the repo

```bash
git clone https://github.com/msv-akshat/AgroScan_AI.git
cd AgroScan_AI
```

### 2. Run the backend locally

```powershell
cd ml_model
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python local_server.py
```

This starts the local API at http://127.0.0.1:8000.

### 3. Run the frontend locally

Open a second terminal:

```powershell
cd frontend
npm install
$env:VITE_BACKEND_URL="http://127.0.0.1:8000"
npm run dev
```

Open the Vite URL shown in the terminal, usually http://localhost:5173.

### 4. Optional production build check

```bash
cd frontend
npm install
npm run build
```

### 5. Deployment

- Deploy the frontend to AWS Amplify for CI/CD from the GitHub `main` branch.
- Build the backend Docker image from `ml_model/Dockerfile` and deploy it to AWS Lambda through API Gateway.


***

## Model Training

- Model training/execution workflow and code:

```
ml_model/notebooks/model_training_notebook.ipynb
```

- CNN (TensorFlow/Keras) achieves ~98% validation accuracy on 38+ classes with augmentation \& normalization.

***

## Planned Improvements

- Error handling for non-image/invalid file uploads
- CLI for simple model retraining and deployment
- Improved UI loading indicators and confidence explanations
- Expanded troubleshooting and FAQ in docs

***

## Author

**Akshat Madamsetty**
AI, Cloud \& Full Stack Developer

- [LinkedIn](https://linkedin.com/in/sai-venkat-akshat-madamsetty-b3242328b/)
- [GitHub](https://github.com/msv-akshat)

***

## License

MIT License

***




