from client import ShapleyCreditAssignment

def main():
    print("=== Testing Cooperative Multi-Agent Shapley Credit Assignment ===")
    sca = ShapleyCreditAssignment()

    def game_reward(coalition):
        val = 0
        if "Agent-A" in coalition: val += 10
        if "Agent-B" in coalition: val += 20
        if "Agent-A" in coalition and "Agent-B" in coalition: val += 30
        return val

    agents = ["Agent-A", "Agent-B"]
    values = sca.compute_shapley_values(agents, game_reward)
    print("Computed Shapley values:", values)
    assert values["Agent-A"] == 25.0
    assert values["Agent-B"] == 35.0
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
