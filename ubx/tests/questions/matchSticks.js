function matchHouses(step) {
  return step === 0 ? 0 : step * 4 + (step + 1);
};

console.log(matchHouses(1));