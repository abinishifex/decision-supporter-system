import React from 'react';
import { Link } from 'react-router-dom';

const HeroSection = () => {
  return (
    <section className="hero-modern">
      <div className="container">
        <div className="hero-pill">
            <span className="hero-pill-dot"></span>
            Elevating Your Decision Process
        </div>
        
        <h1 className="hero-title">
          Decision <span>Supporter</span> System
        </h1>
        
        <p className="hero-subtitle">
          Make smarter decisions with intelligent guidance. Our dynamic framework helps you evaluate options objectively and find the best path forward.
        </p>
        
        <div className="hero-actions">
            <Link to="/decision" className="btn-brand">
              Start Decision Process
            </Link>
            <Link to="/about" className="btn-outline">
              Learn How It Works
            </Link>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
