import React from 'react';
import { Brain, Github, Twitter, Linkedin } from 'lucide-react';
import { Link } from 'react-router-dom';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-grid">
          <div>
            <div className="footer-logo">
              <Brain size={24} />
              <span>DSS</span>
            </div>
            <p className="footer-text">
              Empowering individuals and teams to make smarter, data-driven decisions with intelligent guidance.
            </p>
          </div>
          <div>
            <h4 className="footer-title">Product</h4>
            <ul className="footer-links">
              <li><Link to="/" className="footer-link">Features</Link></li>
              <li><Link to="/decision" className="footer-link">Decision Tool</Link></li>
              <li><Link to="/about" className="footer-link">How it Works</Link></li>
            </ul>
          </div>
          <div>
            <h4 className="footer-title">Company</h4>
            <ul className="footer-links">
              <li><Link to="/about" className="footer-link">About Us</Link></li>
              <li><a href="#" className="footer-link">Contact</a></li>
              <li><a href="#" className="footer-link">Privacy Policy</a></li>
            </ul>
          </div>
          <div>
            <h4 className="footer-title">Social</h4>
            <div style={{ display: 'flex', gap: '1rem' }}>
              <a href="#" className="footer-link"><Twitter size={20} /></a>
              <a href="#" className="footer-link"><Github size={20} /></a>
              <a href="#" className="footer-link"><Linkedin size={20} /></a>
            </div>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; {new Date().getFullYear()} Decision Supporter System. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
