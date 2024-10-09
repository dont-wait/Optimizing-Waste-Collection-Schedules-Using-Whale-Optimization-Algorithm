import { getRandomValue } from "./getRandomValue.js";

class WOA {
  constructor(dim, range, numberOfSols, maxIter, fitnessFunc, limit) {
    this.dim = dim;
    this.range = range;
    this.fitnessFunc = fitnessFunc;
    this.numberOfSols = numberOfSols;
    this.maxIter = maxIter;
    this.bestSol = undefined;
    this.bestFitness = Infinity;
    this.population = undefined;
    this.limit = limit;
  }

  createPopulations() {
    return Array.from({ length: this.numberOfSols }, () =>
      Array.from({ length: this.dim - 1 }, () =>
        Math.floor(getRandomValue(this.range))
      )
    );
  }

  calculateFitness(pop) {
    return pop.map((whale) =>
      this.fitnessFunc([0, ...whale, 0], this.dim, this.limit)
    );
  }

  selectBestFitness(fitnessList) {
    console.log("chon ra fitness tot nhat");
    const minIdx = fitnessList.indexOf(Math.min(...fitnessList));
    const currBestSol = this.population[minIdx];
    const minValue = fitnessList[minIdx];

    if (minValue < this.bestFitness) {
      this.bestSol = currBestSol;
      this.bestFitness = minValue;
    }
  }

  calculate_A(a) {
    return Array.from(
      { length: this.dim - 1 },
      () => 2 * a * Math.random() - a
    );
  }

  calculate_C() {
    return Array.from({ length: this.dim - 1 }, () => 2 * Math.random());
  }

  calculate_D(X_rb, X) {
    const C = this.calculate_C();
    return X_rb.map((x_rb, i) => Math.abs(C[i] * x_rb - X[i]));
  }

  Encircling(X_best, X, A) {
    const D = this.calculate_D(X_best, X);
    return X_best.map((x_best, i) => x_best - A[i] * D[i]);
  }

  Searching(X_rand, X, A) {
    const D = this.calculate_D(X_rand, X);
    return X_rand.map((x_rand, i) => x_rand - A[i] * D[i]);
  }

  Attacking(X_best, X) {
    const D = X_best.map((x_best, i) => Math.abs(x_best - X[i]));
    const l = getRandomValue([-1, 1]);
    return D.map(
      (d, i) => d * Math.exp(1 * l) * Math.cos(2 * Math.PI * l) + X_best[i]
    );
  }

  checking(populations, [lb, ub]) {
    populations.forEach((population) =>
      population.forEach((value, j) => {
        population[j] = Math.max(lb, Math.min(value, ub));
      })
    );
  }

  optimize() {
    const pops_range = [0, this.numberOfSols - 1];
    this.population = this.createPopulations();

    for (let t = 0; t < this.maxIter; t++) {
      let fitnessList = this.calculateFitness(this.population);
      this.selectBestFitness(fitnessList);

      const newPopulation = this.population.map((whale) => {
        const a = 2 * (1 - t / this.maxIter);
        const p = Math.random();

        if (p < 0.5) {
          const A = this.calculate_A(a);
          if (Math.sqrt(A.reduce((total, item) => total + item ** 2, 0) < 1))
            return this.Encircling(this.bestSol, whale, A);
          const X_rand =
            this.population[Math.floor(getRandomValue(pops_range))];
          return this.Searching(X_rand, whale, A);
        } else return this.Attacking(this.bestSol, whale);
      });

      this.checking(newPopulation, this.range);
      newPopulation.forEach((whale) =>
        whale.forEach((val, j) => {
          whale[j] = Math.ceil(val) - 1;
        })
      );
      this.population = newPopulation;
    }
  }
}

export default WOA;
