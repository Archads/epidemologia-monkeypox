import numpy as np
from config import (
    GRID_SIZE,
    S, E, I, R,
    INITIAL_INFECTED,
    P_INFECT,
    P_EXPOSE_TO_INFECT,
    P_RECOVER,
    STEPS,
    CLUSTER_RATIO,
    CLUSTER_INTENSITY
)


class SEIRModel:
    def __init__(self):
        self.N = GRID_SIZE

        # grade começa toda como Suscetível
        self.grid = np.full((self.N, self.N), S, dtype=int)

        # usado para métricas
        self.history = {"S": [], "E": [], "I": [], "R": []}

        # clusters sociais pré-gerados
        self._create_population_with_clusters()

        # infecta alguns indivíduos
        self._infect_initial()


    # -----------------------------------------------------------
    def _create_population_with_clusters(self):
        """
        Gera um mapa booleano indicando quais indivíduos pertencem a clusters.
        Em clusters, a transmissibilidade é maior.
        """
        self.cluster_map = (np.random.random((self.N, self.N)) < CLUSTER_RATIO)


    # -----------------------------------------------------------
    def _infect_initial(self):
        for _ in range(INITIAL_INFECTED):
            x = np.random.randint(0, self.N)
            y = np.random.randint(0, self.N)
            self.grid[x, y] = I


    # -----------------------------------------------------------
    def _count_neighbors(self, x, y, state):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                nx, ny = x + dx, y + dy
                if 0 <= nx < self.N and 0 <= ny < self.N:
                    if self.grid[nx, ny] == state:
                        count += 1
        return count


    # -----------------------------------------------------------
    def _update_cell(self, x, y):
        st = self.grid[x, y]

        # SUSCETÍVEL
        if st == S:
            nI = self._count_neighbors(x, y, I)

            if nI == 0:
                return S

            # probabilidade de infecção
            p = 1 - (1 - P_INFECT)**nI

            # aumento da transmissibilidade em clusters
            if self.cluster_map[x, y]:
                p *= (1 + CLUSTER_INTENSITY)

            return E if (np.random.random() < p) else S

        # EXPOSTO → INFECTADO
        if st == E:
            return I if np.random.random() < P_EXPOSE_TO_INFECT else E

        # INFECTADO → RECUPERADO
        if st == I:
            return R if np.random.random() < P_RECOVER else I

        # RECUPERADO
        return R


    # -----------------------------------------------------------
    def step(self):
        new = np.copy(self.grid)

        for x in range(self.N):
            for y in range(self.N):
                new[x, y] = self._update_cell(x, y)

        self.grid = new
        self._record_history()


    # -----------------------------------------------------------
    def _record_history(self):
        unique, counts = np.unique(self.grid, return_counts=True)
        d = dict(zip(unique, counts))

        self.history["S"].append(d.get(S, 0))
        self.history["E"].append(d.get(E, 0))
        self.history["I"].append(d.get(I, 0))
        self.history["R"].append(d.get(R, 0))


    # -----------------------------------------------------------
    def run(self):
        for _ in range(STEPS):
            self.step()

        return self.history, self.grid