import React from 'react';
import { Trophy } from 'lucide-react';

const ResultCard = ({ name, score, isBest, maxScore }) => {
  const percentage = (score / maxScore) * 100;

  return (
    <div className={`card result-card ${isBest ? 'best' : ''}`}>
      <div className="result-header">
        <h3 style={{ fontWeight: 700 }}>{name}</h3>
        {isBest && <Trophy size={24} color="#3b82f6" />}
      </div>
      <div className="result-score">
        {score} <span style={{ fontSize: '1rem', color: 'var(--text-secondary)', fontWeight: 500 }}>/ {maxScore}</span>
      </div>
      <div className="score-bar-bg">
        <div className="score-bar-fill" style={{ width: `${percentage}%` }}></div>
      </div>
      {isBest && (
        <p style={{ marginTop: '1rem', color: '#3b82f6', fontWeight: 600, fontSize: '0.9rem' }}>
          Recommended Decision
        </p>
      )}
    </div>
  );
};

export default ResultCard;
