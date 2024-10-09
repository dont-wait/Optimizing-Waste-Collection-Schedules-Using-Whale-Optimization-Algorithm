import WOA from "./woa.js";

const dim = 5;
const limit = 100;

function FitnessFunc(whale, dim, limit) {
  const w = [
    [-1, -1, 5, -1, 6],
    [-1, -1, 6, 3, 4],
    [5, 6, -1, -1, -1],
    [-1, 3, -1, -1, 2],
    [6, 4, -1, 2, -1],
  ];

  const l = [0, 90, 60, 20, 10];
  let fx = 0;
  let gx = 0;
  let hx = 0;

  for (let i = 0; i < dim; i++) {
    if (w[whale[i]][whale[i + 1]] == -1) fx++;
  }

  if (fx == 0) {
    let flag = true;
    for (let i = 0; i < dim; i++) {
      gx += w[whale[i]][whale[i + 1]];
      if (hx + l[whale[i]] + l[whale[i + 1]] <= limit && flag) {
        hx = hx + l[whale[i]] + l[whale[i + 1]];
        l[whale[i]] = 0;
        l[whale[i + 1]] = 0;
      } else flag = false;
    }
    console.log(fx, gx, hx);
    return -(hx + 10 / gx);
  }
  return fx;
}

const woa = new WOA(dim, [1, 5], 30, 500, FitnessFunc, limit);

woa.optimize();
console.log(woa.bestFitness);

let res = [0, ...woa.bestSol, 0];

let tmp = 0;
const l = [0, 90, 60, 20, 10];
const v = [false, false, false, false, false];
let breakpoint;

for (let i = 0; i < dim; i++) {
  if (tmp + l[res[i]] + l[res[i + 1]] <= limit) {
    tmp = tmp + l[res[i]] + l[res[i + 1]];
    l[res[i]] = 0;
    l[res[i + 1]] = 0;
    v[res[i]] = true;
    v[res[i + 1]] = true;
  } else {
    breakpoint = res[i];
    break;
  }
}

const w = [
  [-1, -1, 5, -1, 6],
  [-1, -1, 6, 3, 4],
  [5, 6, -1, -1, -1],
  [-1, 3, -1, -1, 2],
  [6, 4, -1, 2, -1],
];

console.log(breakpoint);

document.getElementById("result").innerText = res
  .map((item) => item + 1)
  .join(" ===> ");

document.getElementById("visited").innerText = v
  .map((item, idx) => (item ? idx + 1 : " x "))
  .join(" --- ");
