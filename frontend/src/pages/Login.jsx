import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Brain, Eye, EyeOff, LogIn, UserPlus } from 'lucide-react';
import { loginUser, registerUser } from '../lib/api';

const Login = () => {
  const navigate = useNavigate();
  const [mode, setMode] = useState('login');
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const reset = () => { setError(''); setUsername(''); setEmail(''); setPassword(''); };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      const data = mode === 'login'
        ? await loginUser(username, password)
        : await registerUser(username, password, email);
      localStorage.setItem('username', data.username);
      window.dispatchEvent(new Event('focus'));
      navigate('/decision');
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      minHeight: '100vh',
      background: 'var(--bg-color)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '2rem',
    }}>
      <div style={{ width: '100%', maxWidth: '420px' }}>

        {/* Logo */}
        <div style={{ textAlign: 'center', marginBottom: '2.5rem' }}>
          <Link to="/" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.75rem', color: 'var(--text-primary)' }}>
            <div style={{
              width: '52px', height: '52px',
              background: 'var(--primary-gradient)',
              borderRadius: '0.875rem',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
            }}>
              <Brain size={28} color="white" />
            </div>
            <span style={{ fontSize: '1.8rem', fontWeight: 900 }}>DSS</span>
          </Link>
          <p style={{ color: 'var(--text-secondary)', marginTop: '0.75rem', fontSize: '0.95rem' }}>
            {mode === 'login' ? 'Welcome back. Sign in to continue.' : 'Create your account to get started.'}
          </p>
        </div>

        {/* Card */}
        <div className="card" style={{ padding: '2.5rem' }}>

          {/* Tab toggle */}
          <div style={{
            display: 'flex', gap: '4px',
            background: 'var(--bg-color)',
            borderRadius: '0.75rem',
            padding: '4px',
            marginBottom: '2rem',
          }}>
            {[
              { key: 'login', label: 'Sign In', icon: <LogIn size={15} /> },
              { key: 'register', label: 'Register', icon: <UserPlus size={15} /> },
            ].map(({ key, label, icon }) => (
              <button
                key={key}
                onClick={() => { setMode(key); reset(); }}
                style={{
                  flex: 1, padding: '0.6rem', borderRadius: '0.6rem',
                  fontWeight: 600, fontSize: '0.9rem',
                  display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '6px',
                  background: mode === key ? 'var(--primary-gradient)' : 'transparent',
                  color: mode === key ? 'white' : 'var(--text-secondary)',
                  transition: 'all 0.2s ease',
                }}
              >
                {icon}{label}
              </button>
            ))}
          </div>

          <form onSubmit={handleSubmit}>

            {/* Username */}
            <div className="form-group">
              <label className="form-label">Username</label>
              <input
                className="form-input"
                style={{ width: '100%', display: 'block' }}
                type="text"
                placeholder="Enter your username"
                value={username}
                autoComplete="username"
                onChange={(e) => { setUsername(e.target.value); setError(''); }}
                required
              />
            </div>

            {/* Email — register only */}
            {mode === 'register' && (
              <div className="form-group">
                <label className="form-label">
                  Email <span style={{ color: 'var(--text-secondary)', fontWeight: 400 }}>(optional)</span>
                </label>
                <input
                  className="form-input"
                  style={{ width: '100%', display: 'block' }}
                  type="email"
                  placeholder="you@example.com"
                  value={email}
                  autoComplete="email"
                  onChange={(e) => { setEmail(e.target.value); setError(''); }}
                />
              </div>
            )}

            {/* Password */}
            <div className="form-group">
              <label className="form-label">Password</label>
              <div style={{ position: 'relative' }}>
                <input
                  className="form-input"
                  style={{ width: '100%', display: 'block', paddingRight: '3rem' }}
                  type={showPassword ? 'text' : 'password'}
                  placeholder={mode === 'register' ? 'Min. 6 characters' : 'Enter your password'}
                  value={password}
                  autoComplete={mode === 'login' ? 'current-password' : 'new-password'}
                  onChange={(e) => { setPassword(e.target.value); setError(''); }}
                  required
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  style={{
                    position: 'absolute', right: '0.75rem', top: '50%',
                    transform: 'translateY(-50%)',
                    background: 'none', color: 'var(--text-secondary)',
                  }}
                >
                  {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                </button>
              </div>
            </div>

            {/* Error */}
            {error && (
              <p style={{ color: '#f87171', fontSize: '0.875rem', marginBottom: '1.25rem', textAlign: 'center', fontWeight: 600 }}>
                {error}
              </p>
            )}

            {/* Submit */}
            <button
              type="submit"
              className="btn-primary"
              disabled={loading}
              style={{ width: '100%', padding: '0.9rem', fontSize: '1rem', opacity: loading ? 0.7 : 1 }}
            >
              {loading ? 'Please wait...' : mode === 'login' ? 'Sign In' : 'Create Account'}
            </button>
          </form>
        </div>

        <p style={{ textAlign: 'center', marginTop: '1.5rem', color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
          <Link to="/" style={{ color: 'var(--accent-color)' }}>← Back to Home</Link>
        </p>
      </div>
    </div>
  );
};

export default Login;
