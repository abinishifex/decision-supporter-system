export const calculateScore = (answers) => {
  let score = 0;
  // Answers is now an object of numeric values directly
  Object.values(answers).forEach(val => {
    score += Number(val) || 0;
  });

  return score;
};
