import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { loginUser, registerUser } from '../lib/api';


const initialForm = {
  username: '',
  email: '',
  password: '',
};

const Login = ({ authReady, currentUser, onAuthChange }) => {
  const navigate = useNavigate();
  const [mode, setMode] = useState('login');
  const [form, setForm] = useState(initialForm);
  const [error, setError] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  useEffect(() => {
    if (authReady && currentUser) {
      navigate('/decision', { replace: true });
    }
  }, [authReady, currentUser, navigate]);

  function updateField(field, value) {
    setError('');
    setForm((prev) => ({ ...prev, [field]: value }));
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setError('');
    setIsSubmitting(true);

    try {
      const action = mode === 'login' ? loginUser : registerUser;
      const payload =
        mode === 'login'
          ? { username: form.username, password: form.password }
          : form;
      const data = await action(payload);
      onAuthChange(data.user);
      navigate('/decision');
    } catch (apiError) {
      setError(apiError.message || 'Authentication failed.');
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <section className="section-padding">
      <div className="container">
        <div className="login-shell">
          <div className="login-panel">
            <div className="login-header">
              <p className="login-eyebrow">Account Access</p>
              <h1>{mode === 'login' ? 'Sign in to your account' : 'Create your account'}</h1>
              <p className="login-subtext">
                {mode === 'login'
                  ? 'Use your DSS account to keep working from the decision dashboard.'
                  : 'Create a local account backed by Django session auth.'}
              </p>
            </div>

            <form className="login-form" onSubmit={handleSubmit}>
              <label className="login-label">
                Username
                <input
                  type="text"
                  value={form.username}
                  onChange={(event) => updateField('username', event.target.value)}
                  placeholder="Enter username"
                  required
                />
              </label>

              {mode === 'register' && (
                <label className="login-label">
                  Email
                  <input
                    type="email"
                    value={form.email}
                    onChange={(event) => updateField('email', event.target.value)}
                    placeholder="Enter email"
                    required
                  />
                </label>
              )}

              <label className="login-label">
                Password
                <input
                  type="password"
                  value={form.password}
                  onChange={(event) => updateField('password', event.target.value)}
                  placeholder="Enter password"
                  required
                />
              </label>

              {error && <p className="login-error">{error}</p>}

              <button className="btn-primary login-submit" type="submit" disabled={isSubmitting}>
                {isSubmitting
                  ? 'Please wait...'
                  : mode === 'login'
                    ? 'Login'
                    : 'Create Account'}
              </button>
            </form>

            <div className="login-switch">
              <span>{mode === 'login' ? 'Need an account?' : 'Already have an account?'}</span>
              <button
                type="button"
                className="login-switch-btn"
                onClick={() => {
                  setMode((prev) => (prev === 'login' ? 'register' : 'login'));
                  setForm(initialForm);
                  setError('');
                }}
              >
                {mode === 'login' ? 'Register here' : 'Back to login'}
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Login;
