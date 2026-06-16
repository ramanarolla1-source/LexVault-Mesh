<img width="1024" height="559" alt="LexVault Mesh Distributed Intelligence Architecture" src="https://github.com/user-attachments/assets/aa7f0557-abfc-4068-a74e-7ae61da45e71" />
Demo Video: https://youtu.be/ROpnOzo2Qx0
One Pager: https://docs.google.com/document/d/1YHvCW_hy33WkuP_STpLhAPyzQ9XzxHmrGQRWNTRNUYI/edit?usp=sharing
Presentation Deck: https://docs.google.com/presentation/d/1qJKbG8FVb2lJ3kpMmzYjtvXkWDtqhs13aBk2mU603xQ/edit?usp=sharing

# LexVault Mesh
**Distributed Offline Intelligence for Legal Discovery**

LexVault Mesh is a high-performance, P2P-orchestrated legal intelligence suite. It empowers law firms and investigators to process sensitive case evidence (WhatsApp, PDFs, emails) entirely offline, utilizing a multi-agent mesh of consumer devices.

---

## 🛠 Architecture & Workflow
![LexVault Mesh Distributed Intelligence Architecture.jpg](./docs/LexVault_Mesh_Distributed_Intelligence_Architecture.jpg)

LexVault Mesh implements **Hardware-Matched Delegation** via the QVAC SDK:
*   **Edge Capture (Mobile)**: Optimized OCR and secure evidence ingestion.
*   **Mesh Intelligence (P2P Layer)**: 
    *   **Laptop Agent**: Manages vector embedding generation and RAG retrieval pipelines.
    *   **Desktop Agent**: Executes heavy-duty deep reasoning and contradiction analysis.
*   **Convergence**: Automated synthesis of Knowledge Graphs and Litigation Briefs.

---

## 📋 Hardware Specifications (Reproducibility Proof)
*The following hardware was used for this demonstration. To reproduce these performance logs, ensure your devices meet or exceed these specifications.*

| Node Role | Device | CPU | RAM | VRAM / GPU |
| :--- | :--- | :--- | :--- | :--- |
| **Capture** | iPhone 15 Pro | A17 Pro | 8 GB | N/A |
| **Embedding** | MacBook Pro M3 | M3 | 16 GB | 16 GB Shared |
| **Reasoning** | Custom Desktop | Ryzen 9 | 64 GB | 24 GB (RTX 4090) |

---

## 🚀 Setup & Deployment
### 1. Prerequisites
- **QVAC SDK**: Ensure the environment is configured with `@qvac/sdk`.
- **Network**: All devices must be connected to the same localized P2P mesh network.

### 2. Installation
```bash
git clone [https://github.com/your-username/LexVault-Mesh.git](https://github.com/your-username/LexVault-Mesh.git)
cd LexVault-Mesh
pip install -r requirements.txt
  
  
