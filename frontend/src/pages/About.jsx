import React from 'react';
import { Brain, Target, Zap, CheckCircle2 } from 'lucide-react';

const About = () => {
  return (
    <div className="section-padding page-shell">
      <div className="container">
        <div style={{ textAlign: 'center', marginBottom: '5rem' }}>
          <h1 style={{ fontSize: '3.5rem', fontWeight: 900, marginBottom: '1.5rem' }}>
            About <span className="gradient-text">IDAS</span>
          </h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '1.2rem', maxWidth: '800px', margin: '0 auto' }}>
            The Decision Supporter System (IDAS) was built to bridge the gap between intuition and logic.
          </p>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '4rem', alignItems: 'center', marginBottom: '6rem' }}>
          <div>
            <h2 style={{ fontSize: '2rem', fontWeight: 800, marginBottom: '1.5rem' }}>What is IDAS?</h2>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '1.5rem', fontSize: '1.05rem' }}>
              IDAS is a modern decision-support framework designed to help you navigate complex choices. Whether you're deciding on a career move, a financial investment, or a personal project, our system provides the structure you need.
            </p>
            <p style={{ color: 'var(--text-secondary)', fontSize: '1.05rem' }}>
              By breaking down decisions into quantifiable metrics, we help you see past the noise and focus on what truly matters.
            </p>
          </div>
        <div className="card" style={{ background: 'var(--hero-gradient)', display: 'flex', justifyContent: 'center', padding: '4rem' }}>
          <Brain size={120} color="#3b82f6" />
        </div>
        </div>

        <div style={{ marginBottom: '6rem' }}>
          <h2 style={{ fontSize: '2rem', fontWeight: 800, textAlign: 'center', marginBottom: '4rem' }}>Why Use It?</h2>
          <div className="features-grid">
            <div className="card">
              <Target size={32} color="#3b82f6" style={{ marginBottom: '1rem' }} />
              <h3 style={{ marginBottom: '1rem' }}>Precision</h3>
              <p style={{ color: 'var(--text-secondary)' }}>Move from "gut feeling" to data-backed conclusions.</p>
            </div>
            <div className="card">
              <Zap size={32} color="#3b82f6" style={{ marginBottom: '1rem' }} />
              <h3 style={{ marginBottom: '1rem' }}>Speed</h3>
              <p style={{ color: 'var(--text-secondary)' }}>Reduce analysis paralysis with a guided workflow.</p>
            </div>
            <div className="card">
              <CheckCircle2 size={32} color="#3b82f6" style={{ marginBottom: '1rem' }} />
              <h3 style={{ marginBottom: '1rem' }}>Confidence</h3>
              <p style={{ color: 'var(--text-secondary)' }}>Feel secure in your choices knowing you've evaluated all angles.</p>
            </div>
          </div>
        </div>

        <div className="card" style={{ background: 'rgba(8, 17, 31, 0.92)', padding: '4rem' }}>
          <h2 style={{ fontSize: '2rem', fontWeight: 800, textAlign: 'center', marginBottom: '3rem' }}>How It Works</h2>
          <div style={{ maxWidth: '700px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '2rem' }}>
            <div style={{ display: 'flex', gap: '1.5rem' }}>
              <div style={{ width: '40px', height: '40px', background: 'var(--primary-gradient)', color: 'white', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, fontWeight: 700 }}>1</div>
              <div>
                <h4 style={{ fontWeight: 700, marginBottom: '0.5rem' }}>Input Analysis</h4>
                <p style={{ color: 'var(--text-secondary)' }}>Our system scans your problem for keywords to determine the most relevant evaluation criteria.</p>
              </div>
            </div>
            <div style={{ display: 'flex', gap: '1.5rem' }}>
              <div style={{ width: '40px', height: '40px', background: 'var(--primary-gradient)', color: 'white', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, fontWeight: 700 }}>2</div>
              <div>
                <h4 style={{ fontWeight: 700, marginBottom: '0.5rem' }}>Weighted Scoring</h4>
                <p style={{ color: 'var(--text-secondary)' }}>Each answer is assigned a numerical value (High=3, Medium=2, Low=1) to create an objective score.</p>
              </div>
            </div>
            <div style={{ display: 'flex', gap: '1.5rem' }}>
              <div style={{ width: '40px', height: '40px', background: 'var(--primary-gradient)', color: 'white', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, fontWeight: 700 }}>3</div>
              <div>
                <h4 style={{ fontWeight: 700, marginBottom: '0.5rem' }}>Ranking Engine</h4>
                <p style={{ color: 'var(--text-secondary)' }}>Options are ranked based on their total scores, highlighting the most optimal path.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;
