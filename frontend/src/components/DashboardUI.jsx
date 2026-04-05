import React, { useState } from 'react';
import { Search, PieChart, Settings, FileText, CheckCircle2, X } from 'lucide-react';
import { Link, useNavigate } from 'react-router-dom';
import { motion } from 'motion/react';

const DashboardUI = () => {
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const navigate = useNavigate();

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      // Pass the search query into the decision engine as the initial problem
      navigate('/decision', { state: { initialProblem: searchQuery } });
    }
  };

  return (
    <div className="dash-wrapper">
      <div className="dash-container">
        
        {/* Header Streamlined */}
        <div className="dash-header">
          <div>
            <h2>Decision Support System</h2>
            <p>Smart solutions for better decisions</p>
          </div>
          <div className="dash-icons">
            {isSearchOpen ? (
              <form onSubmit={handleSearch} className="dash-search-form">
                <Search size={16} color="#3b82f6" style={{marginRight: '8px'}} />
                <input 
                  type="text" 
                  autoFocus
                  placeholder="Search models..." 
                  className="dash-search-input"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                />
                <button type="button" onClick={() => setIsSearchOpen(false)} className="dash-search-close">
                  <X size={16} />
                </button>
              </form>
            ) : (
              <button title="Search" onClick={() => setIsSearchOpen(true)} className="dash-icon-btn">
                <Search size={20} />
              </button>
            )}
          </div>
        </div>

        {/* Action Cards */}
        <div className="dash-cards">
          {/* Card 1 */}
          <div className="dash-card">
            <div className="dash-card-icon" style={{background: '#fff7ed', color: '#f97316'}}>
              <PieChart size={30} strokeWidth={2.5} />
            </div>
            <h3 className="dash-card-title">Data Insights</h3>
            <p className="dash-card-desc">Valuable insights to guide your strategy.</p>
            <Link to="/decision" className="dash-btn" style={{background: '#f97316'}}>
              VIEW INSIGHTS &rarr;
            </Link>
          </div>

          {/* Card 2 */}
          <div className="dash-card">
            <div className="dash-card-icon" style={{background: '#eff6ff', color: '#3b82f6'}}>
              <Settings size={30} strokeWidth={2.5} />
            </div>
            <h3 className="dash-card-title">Decision Models</h3>
            <p className="dash-card-desc">Manage your custom criteria logically.</p>
            <Link to="/decision" className="dash-btn" style={{background: '#3b82f6'}}>
              MANAGE MODELS &rarr;
            </Link>
          </div>

          {/* Card 3 */}
          <div className="dash-card">
            <div className="dash-card-icon" style={{background: '#faf5ff', color: '#a855f7'}}>
              <FileText size={30} strokeWidth={2.5} />
            </div>
            <h3 className="dash-card-title">Reports & Results</h3>
            <p className="dash-card-desc">Detailed breakdowns of your choices.</p>
            <Link to="/decision" className="dash-btn" style={{background: '#a855f7'}}>
              DOWNLOAD PDF &rarr;
            </Link>
          </div>
        </div>

        {/* Bottom Section */}
        <div className="dash-bottom">
          {/* Analytics Overview */}
          <div className="dash-analytics">
            <h3 className="dash-analytics-title">Analytics Overview</h3>
            
            <div className="dash-chart">
              <div className="dash-bar" style={{height: '35%'}}></div>
              <div className="dash-bar" style={{height: '65%'}}></div>
              <div className="dash-bar" style={{height: '45%'}}></div>
              <div className="dash-bar active" style={{height: '100%'}}></div>
              <div className="dash-bar" style={{height: '25%'}}></div>
            </div>
            
            <div className="dash-stats">
              <div className="dash-stat-item">
                <div className="dash-stat-value">85%</div>
                <div className="dash-stat-label">Accuracy</div>
              </div>
              <div style={{width: 1, height: 50, background: '#e2e8f0'}}></div>
              <div className="dash-stat-item">
                <div className="dash-stat-value">63%</div>
                <div className="dash-stat-label">Efficiency</div>
              </div>
            </div>
          </div>

          {/* Recommendations */}
          <div className="dash-recommendations">
            <h3 className="dash-rec-title">Recommendations</h3>
            
            <div className="dash-rec-list">
              <div className="dash-rec-item">
                <CheckCircle2 size={22} color="#bfdbfe" />
                <span className="dash-rec-text">Optimal Strategy Identified</span>
              </div>
              <div className="dash-rec-item">
                <CheckCircle2 size={22} color="#bfdbfe" />
                <span className="dash-rec-text">Risk Assessment Complete</span>
              </div>
              <div className="dash-rec-item">
                <CheckCircle2 size={22} color="#bfdbfe" />
                <span className="dash-rec-text">Performance Metrics Logged</span>
              </div>
            </div>
            
            <Link to="/decision" className="dash-rec-btn">
              Execute All Recommendations
            </Link>
          </div>
        </div>

      </div>
    </div>
  );
};

export default DashboardUI;
