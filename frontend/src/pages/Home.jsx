import React from 'react';
import HeroSection from '../components/HeroSection';
import FeatureCard from '../components/FeatureCard';
import { Zap, Shield, BarChart3, Users, Globe, Clock } from 'lucide-react';
import { Link } from 'react-router-dom';


  return (
    <div>
      <HeroSection />
      
      <section className="section-padding">
        <div className="container">
          <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
            <h2 style={{ fontSize: '2.5rem', fontWeight: 800, marginBottom: '1rem' }}>Powerful Features</h2>
            <p style={{ color: 'var(--text-secondary)', maxWidth: '600px', margin: '0 auto' }}>
              Everything you need to navigate complex choices with confidence.
            </p>
          </div>
          <div className="features-grid">
            {features.map((f, i) => (
              <FeatureCard key={i} {...f} />
            ))}
          </div>
        </div>
      </section>

      <section className="section-padding" style={{ background: '#f1f5f9' }}>
        <div className="container">
          <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
            <h2 style={{ fontSize: '2.5rem', fontWeight: 800, marginBottom: '1rem' }}>How It Works</h2>
          </div>
          <div className="features-grid">
            <div className="card" style={{ textAlign: 'center' }}>
              <div style={{ fontSize: '2rem', fontWeight: 900, color: '#3b82f6', marginBottom: '1rem' }}>01</div>
              <h3 style={{ marginBottom: '1rem' }}>Define Problem</h3>
              <p style={{ color: 'var(--text-secondary)' }}>Describe your decision and list the options you're considering.</p>
            </div>
            <div className="card" style={{ textAlign: 'center' }}>
              <div style={{ fontSize: '2rem', fontWeight: 900, color: '#3b82f6', marginBottom: '1rem' }}>02</div>
              <h3 style={{ marginBottom: '1rem' }}>Answer Questions</h3>
              <p style={{ color: 'var(--text-secondary)' }}>Evaluate each option against dynamically generated criteria.</p>
            </div>
            <div className="card" style={{ textAlign: 'center' }}>
              <div style={{ fontSize: '2rem', fontWeight: 900, color: '#3b82f6', marginBottom: '1rem' }}>03</div>
              <h3 style={{ marginBottom: '1rem' }}>Get Results</h3>
              <p style={{ color: 'var(--text-secondary)' }}>Review ranked scores and receive a clear recommendation.</p>
            </div>
          </div>
        </div>
      </section>

      <section className="section-padding">
        <div className="container">
          <div className="card" style={{ background: 'var(--primary-gradient)', color: 'white', textAlign: 'center', padding: '4rem' }}>
            <h2 style={{ fontSize: '2.5rem', fontWeight: 800, marginBottom: '1.5rem' }}>Ready to decide?</h2>
            <p style={{ fontSize: '1.1rem', marginBottom: '2.5rem', opacity: 0.9 }}>
              Join thousands of users making better choices every day.
            </p>
            <Link to="/decision" className="btn-primary" style={{ background: 'white', color: '#3b82f6', padding: '1rem 3rem' }}>
              Get Started Now
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;
