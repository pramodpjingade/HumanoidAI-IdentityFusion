# Humanoid AI – Multimodal Identity Fusion

An AI-powered multimodal identity recognition system for humanoid robots that combines facial recognition and voice recognition to identify individuals more reliably.

## Overview

The system integrates two independent biometric recognition modules:

- **Face Recognition:** Identifies individuals using facial features.
- **Voice Recognition:** Identifies individuals using unique voice characteristics.

The Identity Fusion module compares both recognition results and determines the final identity status.

## Features

- Integration of face and voice recognition
- Independent face and voice identification
- Multimodal identity matching
- Identity mismatch detection
- Face-only and voice-only identification
- Unknown identity detection
- Modular architecture
- Test cases for identity fusion

## Technologies Used

- Python 3.11
- OpenCV
- InsightFace
- NumPy
- ONNX Runtime
- PyTorch
- SpeechBrain
- ECAPA-TDNN
- Computer Vision
- Deep Learning

## Project Structure

```text
HumanoidAI-IdentityFusion/
│
├── face_recognition/
│   ├── face_test.py
│   ├── recognition_log.py
│   ├── recognize_face.py
│   ├── register_face.py
│   └── webcam_face_detection.py
│
├── voice_recognition/
│   ├── generate_voice_embeddings.py
│   ├── recognize_voice_clean.py
│   ├── register_voice.py
│   └── other voice modules
│
├── integration/
│   ├── face_adapter.py
│   ├── voice_adapter.py
│   ├── identity_fusion.py
│   └── identity_coordinator.py
│
├── tests/
│   └── test_identity_fusion.py
│
├── requirements.txt
└── README.md
```

## Identity Fusion Logic

The system supports five possible outcomes:

| Status | Description |
|---|---|
| MATCH | Face and voice identify the same person. |
| MISMATCH | Face and voice identify different people. |
| FACE_ONLY | Only face recognition identifies a person. |
| VOICE_ONLY | Only voice recognition identifies a person. |
| UNKNOWN | Neither module identifies a known person. |

## System Workflow

1. Capture a person's face through a camera.
2. Identify the face using the face recognition module.
3. Capture speech through a microphone.
4. Identify the speaker using the voice recognition module.
5. Send both results to the Identity Fusion module.
6. Compare the identities.
7. Generate the final identity status.

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd HumanoidAI-IdentityFusion
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install compatible CUDA-enabled PyTorch and torchaudio builds separately if required.

## Run the System

From the project root:

```bash
python -m integration.identity_coordinator
```

The system requires the appropriate local face and voice databases, model files, webcam, and microphone to be configured.

## Run Identity Fusion Tests

```bash
python -m tests.test_identity_fusion
```

## Applications

- Humanoid robots
- Personalized human–robot interaction
- Multimodal biometric identification
- Intelligent reception robots
- Human-aware robotic systems

## Future Improvements

- Real-time simultaneous face and voice recognition
- Improved identity verification
- AI-powered conversational interaction
- Robot response based on recognized identity
- Integration with an intelligent voice assistant
- Enhanced biometric security

## Privacy and Security

Facial images, voice recordings, and biometric embeddings are sensitive personal data. Protect these files and obtain permission before collecting or sharing them.

## Project Status

Under development as part of a Humanoid Robotics and Artificial Intelligence project.
