import sys
import json
from client import ShapleyCreditAssignment

sca = ShapleyCreditAssignment()

def handle_call(name, arguments):
    if name == "compute":
        agents = arguments["agents"]
        weights = arguments.get("weights", {a: 1.0 for a in agents})
        res = sca.compute_shapley_values(agents, lambda c: sum(weights.get(a, 0.0) for a in c))
        return {"shapley_values": res}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
