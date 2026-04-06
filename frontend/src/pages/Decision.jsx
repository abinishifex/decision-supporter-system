  import React, { useState } from 'react';
  import { useLocation } from 'react-router-dom';
  import OptionInput from '../components/OptionInput';
  import QuestionCard from '../components/QuestionCard';
  import ResultCard from '../components/ResultCard';
  import { categories } from '../utils/questionGenerator';
  import { evaluateDecision } from '../lib/api';
  import { Sparkles, Info, ArrowRight, ArrowLeft, CheckCircle2 } from 'lucide-react';

  const Decision = () => {
    const location = useLocation();
    const [step, setStep] = useState(1); 
    const [problem, setProblem] = useState(location.state?.initialProblem || '');
    const [options, setOptions] = useState(['', '']);
    const [selectedCategory, setSelectedCategory] = useState(null);
    const [answers, setAnswers] = useState({});   
    const [results, setResults] = useState(null);
    const [analysis, setAnalysis] = useState('');
    const [maxScore, setMaxScore] = useState(0);
    const [decisionId, setDecisionId] = useState(null);
    const [error, setError] = useState('');
    const [isSubmitting, setIsSubmitting] = useState(false);

    const handleAddOption = () => setOptions([...options, '']);
    const handleRemoveOption = (index) => setOptions(options.filter((_, i) => i !== index));
    const handleOptionChange = (index, value) => {
      setError('');
      const newOptions = [...options];
      newOptions[index] = value;
      setOptions(newOptions);
    };

    const handleAnswer = (optionIndex, questionId, value) => {
      setError('');
      setAnswers({
        ...answers,
        [optionIndex]: {
          ...(answers[optionIndex] || {}),
          [questionId]: value
        }
      });
    };

    const handleCalculate = async () => {
      setError('');
      setIsSubmitting(true);

      try {
        const data = await evaluateDecision({
          problem,
          options,
          category: selectedCategory,
          answers
        });

        setResults(data.results);
        setAnalysis(data.analysis);
        setMaxScore(data.maxScore);
        setDecisionId(data.decisionId);
        setStep(4);
      } catch (apiError) {
        setError(apiError.message || 'Failed to evaluate your decision.');
      } finally {
        setIsSubmitting(false);
      }
    };

    const isStep1Complete = () => problem.trim().length > 5 && options.every(opt => opt.trim().length > 0);
    const isStep3Complete = () => {
      if (!selectedCategory) return false;
      for (let i = 0; i < options.length; i++) {
        const optionAnswers = answers[i] || {};
        if (Object.keys(optionAnswers).length < selectedCategory.questions.length) return false;
      }
      return true;
    };

    return (
      <div className="section-padding">
        <div className="container">
          <div className="decision-container">
            
            {/* Progress Indicator */}
            <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem', marginBottom: '4rem' }}>
              {[1, 2, 3, 4].map(i => (
                <div 
                  key={i} 
                  style={{ 
                    width: '40px', 
                    height: '40px', 
                    borderRadius: '50%', 
                    background: step >= i ? 'var(--primary-gradient)' : '#e2e8f0',
                    color: 'white',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontWeight: 700,
                    fontSize: '0.9rem'
                  }}
                >
                  {step > i ? <CheckCircle2 size={20} /> : i}
                </div>
              ))}
            </div>

            {step === 1 && (
              <div className="card">
                <h2 style={{ fontSize: '2rem', fontWeight: 800, marginBottom: '2rem', textAlign: 'center' }}>Step 1: Define Decision</h2>
                <div className="form-group">
                  <label className="form-label">What is your decision problem?</label>
                  <textarea
                    className="form-textarea"
                    placeholder="e.g., Should I invest in a new laptop or save for a vacation?"
                    value={problem}
                    onChange={(e) => setProblem(e.target.value)}
                  />
                </div>
                <OptionInput
                  options={options}
                  onAdd={handleAddOption}
                  onRemove={handleRemoveOption}
                  onChange={handleOptionChange}
                />
                <button 
                  className="btn-primary" 
                  style={{ width: '100%', marginTop: '2rem', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}
                  disabled={!isStep1Complete()}
                  onClick={() => setStep(2)}
                >
                  Next: Choose Category <ArrowRight size={20} />
                </button>
              </div>
            )}

            {step === 2 && (
              <div>
                <h2 style={{ fontSize: '2rem', fontWeight: 800, marginBottom: '1rem', textAlign: 'center' }}>Step 2: Select Category</h2>
                <p style={{ textAlign: 'center', color: 'var(--text-secondary)', marginBottom: '3rem' }}>Choose the area that best fits your decision problem.</p>
                
                <div className="category-grid">
                  {categories.map(cat => (
                    <div 
                      key={cat.id} 
                      className={`card category-card ${selectedCategory?.id === cat.id ? 'selected' : ''}`}
                      onClick={() => {
                        setError('');
                        setSelectedCategory(cat);
                      }}
                    >
                      <div className="category-icon">{cat.icon}</div>
                      <div className="category-name">{cat.name}</div>
                      <div className="category-desc">{cat.description}</div>
                    </div>
                  ))}
                </div>

                <div style={{ display: 'flex', gap: '1rem', marginTop: '3rem' }}>
                  <button className="btn-secondary" onClick={() => setStep(1)} style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}>
                    <ArrowLeft size={20} /> Back
                  </button>
                  <button 
                    className="btn-primary" 
                    style={{ flex: 2, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}
                    disabled={!selectedCategory}
                    onClick={() => setStep(3)}
                  >
                    Next: Answer Questions <ArrowRight size={20} />
                  </button>
                </div>
              </div>
            )}

            {step === 3 && (
              <div>
                <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
                  <h2 style={{ fontSize: '2rem', fontWeight: 800, marginBottom: '0.5rem' }}>Step 3: Evaluation</h2>
                  <p style={{ color: 'var(--text-secondary)' }}>Evaluating options for <span style={{ color: 'var(--accent-color)', fontWeight: 700 }}>{selectedCategory.name}</span></p>
                </div>

                {options.map((option, optIndex) => (
                  <div key={optIndex} style={{ marginBottom: '4rem' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '2rem' }}>
                      <div style={{ width: '3rem', height: '3rem', background: 'var(--primary-gradient)', color: 'white', borderRadius: '0.75rem', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 800, fontSize: '1.2rem' }}>
                        {String.fromCharCode(65 + optIndex)}
                      </div>
                      <h3 style={{ fontSize: '1.5rem', fontWeight: 800 }}>{option}</h3>
                    </div>
                    
                    {selectedCategory.questions.map((q) => (
                      <QuestionCard
                        key={q.id}
                        question={q.text}
                        options={q.options}
                        currentAnswer={answers[optIndex]?.[q.id]}
                        onAnswer={(val) => handleAnswer(optIndex, q.id, val)}
                      />
                    ))}
                  </div>
                ))}

                <div style={{ display: 'flex', gap: '1rem', marginTop: '3rem' }}>
                  <button className="btn-secondary" onClick={() => setStep(2)} style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}>
                    <ArrowLeft size={20} /> Back
                  </button>
                  <button 
                    className="btn-primary" 
                    style={{ flex: 2, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}
                    disabled={!isStep3Complete() || isSubmitting}
                    onClick={handleCalculate}
                  >
                    {isSubmitting ? 'Calculating...' : 'Calculate Results'} <Sparkles size={20} />
                  </button>
                </div>
                {error && (
                  <p style={{ color: '#dc2626', marginTop: '1rem', textAlign: 'center', fontWeight: 600 }}>
                    {error}
                  </p>
                )}
              </div>
            )}

            {step === 4 && results && (
              <div>
                <h2 style={{ fontSize: '2.5rem', fontWeight: 900, textAlign: 'center', marginBottom: '4rem' }}>Final Results</h2>
                
                <div className="card" style={{ background: 'var(--primary-gradient)', color: 'white', padding: '3rem', textAlign: 'center', marginBottom: '4rem', borderRadius: '2rem' }}>
                  <h3 style={{ fontSize: '1.25rem', opacity: 0.9, marginBottom: '1rem', fontWeight: 600 }}>Recommended Decision</h3>
                  <div style={{ fontSize: '3rem', fontWeight: 900, marginBottom: '1.5rem' }}>{results[0].name}</div>
                  <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', background: 'rgba(255,255,255,0.2)', padding: '0.5rem 1.5rem', borderRadius: '1rem', fontWeight: 700 }}>
                    Score: {results[0].score} / {maxScore}
                  </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem', marginBottom: '4rem' }}>
                  {results.map((res, i) => (
                    <ResultCard key={i} name={res.name} score={res.score} isBest={i === 0} maxScore={maxScore} />
                  ))}
                </div>

                <div className="card" style={{ background: '#f8fafc', padding: '3rem' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginBottom: '1.5rem' }}>
                    <Info size={24} color="var(--accent-color)" />
                    <h4 style={{ fontSize: '1.25rem', fontWeight: 800 }}>AI Decision Analysis</h4>
                  </div>
                  <p style={{ color: 'var(--text-secondary)', lineHeight: 1.8, fontSize: '1rem' }}>
                    {analysis}
                  </p>
                  {decisionId && (
                    <p style={{ color: 'var(--text-secondary)', marginTop: '1rem', fontSize: '0.9rem' }}>
                      Saved as session #{decisionId}
                    </p>
                  )}
                </div>

                <button 
                  className="btn-secondary" 
                  style={{ width: '100%', marginTop: '3rem', padding: '1.25rem' }}
                  onClick={() => {
                    setStep(1);
                    setProblem('');
                    setOptions(['', '']);
                    setAnswers({});
                    setResults(null);
                    setAnalysis('');
                    setMaxScore(0);
                    setDecisionId(null);
                    setError('');
                    setSelectedCategory(null);
                  }}
                >
                  Start New Decision
                </button>
              </div>
            )}

          </div>
        </div>
      </div>
    );
  };

  export default Decision;
