import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Chatbot from './components/Chatbot';
import Home from './pages/Home';
import About from './pages/About';
import Decision from './pages/Decision';
import Login from './pages/Login';
import { getCurrentUser, logoutUser } from './lib/api';

import './styles/global.css';
import './styles/components.css';

function App() {
  const [currentUser, setCurrentUser] = useState(null);
  const [authReady, setAuthReady] = useState(false);

  useEffect(() => {
    let active = true;

    async function loadUser() {
      try {
        const data = await getCurrentUser();
        if (active) {
          setCurrentUser(data.user);
        }
      } catch {
        if (active) {
          setCurrentUser(null);
        }
      } finally {
        if (active) {
          setAuthReady(true);
        }
      }
    }

    loadUser();

    return () => {
      active = false;
    };
  }, []);

  async function handleLogout() {
    try {
      await logoutUser();
    } finally {
      setCurrentUser(null);
    }
  }

  return (
    <Router>
      <div className="app-wrapper">
        <Navbar currentUser={currentUser} onLogout={handleLogout} />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/decision" element={<Decision />} />
            <Route
              path="/login"
              element={
                <Login
                  authReady={authReady}
                  currentUser={currentUser}
                  onAuthChange={setCurrentUser}
                />
              }
            />
          </Routes>
        </main>
        <Footer />
        <Chatbot />
      </div>
    </Router>
  );
}

export default App;
