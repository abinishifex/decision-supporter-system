import React from 'react';

const QuestionCard = ({ question, options, onAnswer, currentAnswer }) => {
  return (
    <div className="card question-card">
      <p className="question-text">{question}</p>
      <div className="answer-buttons">
        {options.map((opt, index) => (
          <button
            key={index}
            className={`answer-btn ${currentAnswer === opt.value ? 'active' : ''}`}
            onClick={() => onAnswer(opt.value)}
          >
            {opt.label}
          </button>
        ))}
      </div>
    </div>
  );
};

export default QuestionCard;
