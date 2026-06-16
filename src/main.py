"""
LexVault Mesh - Core Entry Point
Initializes the Multi-Agent Mesh and starts the P2P delegation engine.
"""

from qvac.sdk import Mesh, AgentManager
from agents.evidence_agent import EvidenceAgent
from agents.timeline_agent import TimelineAgent
from agents.contradiction_agent import ContradictionAgent
from agents.orchestration_agent import OrchestrationAgent

def main():
    # 1. Initialize the P2P Mesh network
    mesh = Mesh(mode="local_peer")
    
    # 2. Register specialized agents
    manager = AgentManager(mesh)
    manager.register(EvidenceAgent())
    manager.register(TimelineAgent())
    manager.register(ContradictionAgent())
    manager.register(OrchestrationAgent())
    
    print("LexVault Mesh Initialized. Node Active.")
    
    # 3. Start the asynchronous orchestration loop
    # This maintains the continuous state across devices
    manager.run_event_loop()

if __name__ == "__main__":
    main()
