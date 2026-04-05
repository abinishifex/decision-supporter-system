import React from 'react';
import HeroSection from '../components/HeroSection';
import DashboardUI from '../components/DashboardUI';
import FeatureCard from '../components/FeatureCard';
import { Zap, Shield, BarChart3, Users, Globe, Clock } from 'lucide-react';
import { Link } from 'react-router-dom';

const Home = () => {
  const features = [
    { icon: Zap, title: "Dynamic Logic", description: "Our system adapts questions based on your specific problem context." },
    { icon: Shield, title: "Objective Analysis", description: "Remove emotional bias from your decision-making process." },
    { icon: BarChart3, title: "Visual Scoring", description: "See clear rankings and scores for all your options." },
    { icon: Users, title: "Team Ready", description: "Perfect for individual choices or collaborative team decisions." },
    { icon: Globe, title: "Access Anywhere", description: "Cloud-based tool available on all your devices." },
    { icon: Clock, title: "Save Time", description: "Reach conclusions faster with structured evaluation." }
  ];

  return (
    <div className="bg-slate-50 min-h-screen flex flex-col">
      <HeroSection />
      
      {/* Dashboard Preview Section (Based on mockups) */}
      <section className="py-8 bg-slate-50">
        <DashboardUI />
      </section>
      
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
