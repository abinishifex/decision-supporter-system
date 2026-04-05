import React from 'react';
import { Link } from 'react-router-dom';
import { Brain } from 'lucide-react';

const Navbar = () => {
  return (
    <nav className="nav-modern">
      <div className="container">
        <Link to="/" className="nav-logo-modern">
          <div className="nav-logo-icon">
            <Brain size={24} strokeWidth={2.5} />
          </div>
          <span>DSS</span>
        </Link>
        <div className="nav-links-modern">
          <Link to="/" className="nav-link-modern">Home</Link>
          <Link to="/about" className="nav-link-modern">About</Link>
          <Link to="/decision" className="nav-link-modern">Decision</Link>
        </div>
        <div>
          <Link to="/decision" className="btn-primary-modern">
            Get Started
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
