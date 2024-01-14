import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from listeners.handlers import cost

def listener(app):
    app.command("/cost")(
        ack=respond_to_cost_within_3_seconds,  
        lazy=[cost.handler]  
    )

def respond_to_cost_within_3_seconds(ack):
    ack()