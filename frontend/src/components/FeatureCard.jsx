import React from 'react';

const FeatureCard = ({ icon: Icon, title, description }) => {
  return (
    <div className="card feature-card">
      <div className="feature-icon">
        <Icon size={24} />
      </div>
      <h3 style={{ marginBottom: '1rem', fontWeight: 700 }}>{title}</h3>
      <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>{description}</p>
    </div>
  );
};

export default FeatureCard;
