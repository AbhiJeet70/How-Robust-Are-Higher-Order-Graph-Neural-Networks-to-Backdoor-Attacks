# models/__init__.py
from .esan import ESAN
from .sun import SUN, SUNLayer      # SUN model and layer
from .sagn import SubstructureAwareGNN  # SAGN model
from .gnn import GNN                # Generic GNN model
from .trigger import TriggerGenerator
from .ood_detector import OODDetector, Encoder, Decoder
