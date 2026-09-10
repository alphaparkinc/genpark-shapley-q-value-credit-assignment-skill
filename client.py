import itertools

class ShapleyCreditAssignment:
    """
    Cooperative Multi-Agent Shapley Value Credit Assignment.
    Computes fair marginal reward contribution of each agent i across all agent coalitions S.
    """
    def compute_shapley_values(self, agents, characteristic_fn):
        n = len(agents)
        shapley = {a: 0.0 for a in agents}
        all_perms = list(itertools.permutations(agents))

        for perm in all_perms:
            coalition = []
            prev_val = characteristic_fn(coalition)
            for agent in perm:
                coalition.append(agent)
                curr_val = characteristic_fn(coalition)
                marginal = curr_val - prev_val
                shapley[agent] += marginal
                prev_val = curr_val

        for a in agents:
            shapley[a] /= len(all_perms)

        return shapley
