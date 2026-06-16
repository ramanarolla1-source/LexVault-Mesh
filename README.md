<img width="1024" height="559" alt="LexVault Mesh Distributed Intelligence Architecture" src="https://github.com/user-attachments/assets/aa7f0557-abfc-4068-a74e-7ae61da45e71" />
Demo Video: https://youtu.be/ROpnOzo2Qx0
One Pager: https://docs.google.com/document/d/1YHvCW_hy33WkuP_STpLhAPyzQ9XzxHmrGQRWNTRNUYI/edit?usp=sharing
Presentation Deck: https://docs.google.com/presentation/d/1qJKbG8FVb2lJ3kpMmzYjtvXkWDtqhs13aBk2mU603xQ/edit?usp=sharing
LexVault Mesh
Distributed, Sovereign, and Private Legal Intelligence.

LexVault Mesh is a P2P multi-agent network that performs autonomous legal evidence synthesis entirely on-device, ensuring zero data egress to the cloud.
🚀 Key Features
Zero-Cloud Exposure: All RAG, embedding, and reasoning workloads run locally via QVAC SDK.

Multi-Agent Orchestration: Specialized agents for Evidence Extraction, Timeline Synthesis, and Contradiction Detection.

Audit-Ready: Built-in performance telemetry for transparent artifact verification.
🛠 Architecture
Evidence Agent: Performs secure local OCR and entity extraction.

Timeline Agent: Builds chronological event graphs from unstructured evidence.

Contradiction Agent: Uses local reasoning to flag logical inconsistencies.

Orchestration Agent: Handles P2P node discovery and hardware-matched workload delegation.
📋 Hardware Reproducibility
Node Role,Device Model,CPU,RAM,VRAM / GPU
Edge Capture,iPhone 15 Pro,A17 Pro,8 GB,N/A
Embedding,MacBook Pro M3,M3,16 GB,16 GB (Unified)
Reasoning,Custom Build,Ryzen 9 7950X,64 GB,24 GB (RTX 4090)
🛠️ Quick Start Instructions
Clone & Install: Clone the repository and install dependencies from requirements.txt.

Configure: Copy .env.example to .env and set your NODE_ROLE (e.g., laptop).

Initialize: Run the mesh entry point via python src/main.py.
⚖️ Compliance & Auditing
API Disclosure: See api_disclosure.json for proof of zero remote dependencies and 100% local operation.

Performance Logs: See logs/performance_audit.json for benchmark data including TTFT, tokens/sec, and model lifecycles for your demo run.

Prior Work: This project uses the QVAC SDK as its foundational communication layer; all agentic orchestration, logic, and audit-tooling are original contributions created for this hackathon.
