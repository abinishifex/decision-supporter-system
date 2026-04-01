import React from 'react';
import { Link } from 'react-router-dom';
//import { ArrowRight } from 'lucide-react';

const HeroSection = () => {
  return (
    <section className="hero">
      <div className="container">
        <h1>
          Decision <span className="gradient-text">Supporter</span> System
        </h1>
        <p>
          Make smarter decisions with intelligent guidance. Our dynamic framework helps you evaluate options objectively and find the best path forward.
        </p>
        <Link to="/decision" className="btn-primary" style={{ padding: '1rem 2.5rem', fontSize: '1.1rem' }}>
          Start Decision 
          {/* <ArrowRight size={10} style={{ marginLeft: '0.5rem', verticalAlign: 'middle' }} /> */}
        </Link>
      </div>
    </section>
  );
};

export default HeroSection;
