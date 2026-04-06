import React from 'react';
import { Link } from 'react-router-dom';
import { Brain } from 'lucide-react';

const Navbar = ({ currentUser, onLogout }) => {
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
          <Link to="/login" className="nav-link-modern">Login</Link>
        </div>
        {currentUser ? (
          <div className="nav-auth">
            <span className="nav-user">Hi, {currentUser.username}</span>
            <button type="button" className="btn-secondary nav-logout" onClick={onLogout}>
              Logout
            </button>
          </div>
        ) : (
          <div>
            <Link to="/login" className="btn-primary-modern">
              Sign In
            </Link>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
