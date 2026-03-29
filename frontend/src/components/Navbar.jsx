import React from 'react';
import { Link } from 'react-router-dom';
import { Brain } from 'lucide-react';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="container">
        <Link to="/" className="nav-logo">
          <Brain size={32} />
          <span>DSS</span>
        </Link>
        <div className="nav-links">
          <Link to="/" className="nav-link">Home</Link>
          <Link to="/about" className="nav-link">About</Link>
          <Link to="/decision" className="nav-link">Decision</Link>
        </div>
        <Link to="/decision" className="btn-primary" style={{ background: 'white', color: '#3b82f6' }}>
          Get Started
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;
