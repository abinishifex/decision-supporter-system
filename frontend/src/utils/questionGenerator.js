export const categories = [
  {
    id: 'finance',
    name: 'Finance',
    icon: '💰',
    description: 'Investment, saving, business decisions',
    questions: [
      { id: 1, text: "What is the expected ROI?", options: [{label: 'High (>15%)', value: 3}, {label: 'Moderate (5-15%)', value: 2}, {label: 'Low (<5%)', value: 1}] },
      { id: 2, text: "What is your risk tolerance?", options: [{label: 'Aggressive', value: 3}, {label: 'Balanced', value: 2}, {label: 'Conservative', value: 1}] },
      { id: 3, text: "How quickly do you need returns?", options: [{label: 'Long-term (5+ yrs)', value: 3}, {label: 'Mid-term (2-5 yrs)', value: 2}, {label: 'Short-term (<2 yrs)', value: 1}] },
      { id: 4, text: "Initial capital requirement?", options: [{label: 'Low', value: 3}, {label: 'Medium', value: 2}, {label: 'High', value: 1}] },
      { id: 5, text: "Liquidity level?", options: [{label: 'High', value: 3}, {label: 'Medium', value: 2}, {label: 'Low', value: 1}] },
      { id: 6, text: "Market volatility impact?", options: [{label: 'Minimal', value: 3}, {label: 'Moderate', value: 2}, {label: 'Significant', value: 1}] },
      { id: 7, text: "Tax efficiency?", options: [{label: 'Very Efficient', value: 3}, {label: 'Standard', value: 2}, {label: 'Inefficient', value: 1}] },
      { id: 8, text: "Passive income potential?", options: [{label: 'High', value: 3}, {label: 'Medium', value: 2}, {label: 'None', value: 1}] },
      { id: 9, text: "Inflation protection?", options: [{label: 'Strong', value: 3}, {label: 'Moderate', value: 2}, {label: 'Weak', value: 1}] },
      { id: 10, text: "Diversification benefit?", options: [{label: 'Excellent', value: 3}, {label: 'Good', value: 2}, {label: 'Low', value: 1}] }
    ]
  },
  {
    id: 'career',
    name: 'Career',
    icon: '💼',
    description: 'Job choice, career path, switching fields',
    questions: [
      { id: 1, text: "Level of passion for this role?", options: [{label: 'Very High', value: 3}, {label: 'Moderate', value: 2}, {label: 'Low', value: 1}] },
      { id: 2, text: "Salary growth potential?", options: [{label: 'Exponential', value: 3}, {label: 'Steady', value: 2}, {label: 'Limited', value: 1}] },
      { id: 3, text: "Work-life balance?", options: [{label: 'Excellent', value: 3}, {label: 'Manageable', value: 2}, {label: 'Poor', value: 1}] },
      { id: 4, text: "Job security/Stability?", options: [{label: 'High', value: 3}, {label: 'Medium', value: 2}, {label: 'Low', value: 1}] },
      { id: 5, text: "Skill development opportunities?", options: [{label: 'Abundant', value: 3}, {label: 'Some', value: 2}, {label: 'Few', value: 1}] },
      { id: 6, text: "Company culture fit?", options: [{label: 'Perfect', value: 3}, {label: 'Neutral', value: 2}, {label: 'Mismatched', value: 1}] },
      { id: 7, text: "Remote work flexibility?", options: [{label: 'Fully Remote', value: 3}, {label: 'Hybrid', value: 2}, {label: 'On-site', value: 1}] },
      { id: 8, text: "Networking potential?", options: [{label: 'High', value: 3}, {label: 'Medium', value: 2}, {label: 'Low', value: 1}] },
      { id: 9, text: "Impact on long-term goals?", options: [{label: 'Directly Aligned', value: 3}, {label: 'Somewhat', value: 2}, {label: 'Irrelevant', value: 1}] },
      { id: 10, text: "Stress level?", options: [{label: 'Low', value: 3}, {label: 'Moderate', value: 2}, {label: 'High', value: 1}] }
    ]
  },
  {
    id: 'education',
    name: 'Education',
    icon: '📚',
    description: 'Courses, learning paths, skills',
    questions: [
      { id: 1, text: "Market demand for this skill?", options: [{label: 'High', value: 3}, {label: 'Growing', value: 2}, {label: 'Niche', value: 1}] },
      { id: 2, text: "Cost vs. Value ratio?", options: [{label: 'Excellent', value: 3}, {label: 'Fair', value: 2}, {label: 'Expensive', value: 1}] },
      { id: 3, text: "Time commitment required?", options: [{label: 'Flexible', value: 3}, {label: 'Moderate', value: 2}, {label: 'Intensive', value: 1}] },
      { id: 4, text: "Credential recognition?", options: [{label: 'Global', value: 3}, {label: 'Regional', value: 2}, {label: 'None', value: 1}] },
      { id: 5, text: "Prerequisite difficulty?", options: [{label: 'Easy', value: 3}, {label: 'Moderate', value: 2}, {label: 'Hard', value: 1}] },
      { id: 6, text: "Practical application?", options: [{label: 'Immediate', value: 3}, {label: 'Theoretical', value: 2}, {label: 'Abstract', value: 1}] },
      { id: 7, text: "Learning style match?", options: [{label: 'Perfect', value: 3}, {label: 'Good', value: 2}, {label: 'Poor', value: 1}] },
      { id: 8, text: "Peer support/Community?", options: [{label: 'Strong', value: 3}, {label: 'Average', value: 2}, {label: 'Weak', value: 1}] },
      { id: 9, text: "Future-proofing potential?", options: [{label: 'High', value: 3}, {label: 'Moderate', value: 2}, {label: 'Low', value: 1}] },
      { id: 10, text: "Personal interest level?", options: [{label: 'Obsessed', value: 3}, {label: 'Interested', value: 2}, {label: 'Curious', value: 1}] }
    ]
  },
  {
    id: 'business',
    name: 'Business',
    icon: '🚀',
    description: 'Starting a business, scaling, partnerships',
    questions: [
      { id: 1, text: "Scalability potential?", options: [{label: 'Infinite', value: 3}, {label: 'Moderate', value: 2}, {label: 'Linear', value: 1}] },
      { id: 2, text: "Competitive advantage?", options: [{label: 'Strong Moat', value: 3}, {label: 'Some Edge', value: 2}, {label: 'Crowded', value: 1}] },
      { id: 3, text: "Customer acquisition cost?", options: [{label: 'Low', value: 3}, {label: 'Average', value: 2}, {label: 'High', value: 1}] },
      { id: 4, text: "Operational complexity?", options: [{label: 'Simple', value: 3}, {label: 'Moderate', value: 2}, {label: 'Complex', value: 1}] },
      { id: 5, text: "Regulatory hurdles?", options: [{label: 'None', value: 3}, {label: 'Few', value: 2}, {label: 'Many', value: 1}] },
      { id: 6, text: "Profit margin potential?", options: [{label: 'High (>40%)', value: 3}, {label: 'Healthy (15-40%)', value: 2}, {label: 'Thin (<15%)', value: 1}] },
      { id: 7, text: "Founder-market fit?", options: [{label: 'Expert', value: 3}, {label: 'Experienced', value: 2}, {label: 'Novice', value: 1}] },
      { id: 8, text: "Funding requirement?", options: [{label: 'Bootstrapped', value: 3}, {label: 'Seed needed', value: 2}, {label: 'Heavy VC', value: 1}] },
      { id: 9, text: "Exit strategy clarity?", options: [{label: 'Clear', value: 3}, {label: 'Vague', value: 2}, {label: 'None', value: 1}] },
      { id: 10, text: "Market timing?", options: [{label: 'Perfect', value: 3}, {label: 'Early', value: 2}, {label: 'Late', value: 1}] }
    ]
  },
  {
    id: 'relationships',
    name: 'Relationships',
    icon: '❤️',
    description: 'Friends, partners, social decisions',
    questions: [
      { id: 1, text: "Trust level?", options: [{label: 'Absolute', value: 3}, {label: 'Building', value: 2}, {label: 'Low', value: 1}] },
      { id: 2, text: "Communication quality?", options: [{label: 'Open/Honest', value: 3}, {label: 'Average', value: 2}, {label: 'Strained', value: 1}] },
      { id: 3, text: "Shared values?", options: [{label: 'Identical', value: 3}, {label: 'Mostly', value: 2}, {label: 'Few', value: 1}] },
      { id: 4, text: "Emotional support?", options: [{label: 'Consistently', value: 3}, {label: 'Sometimes', value: 2}, {label: 'Rarely', value: 1}] },
      { id: 5, text: "Conflict resolution style?", options: [{label: 'Healthy', value: 3}, {label: 'Avoidant', value: 2}, {label: 'Toxic', value: 1}] },
      { id: 6, text: "Long-term compatibility?", options: [{label: 'High', value: 3}, {label: 'Moderate', value: 2}, {label: 'Low', value: 1}] },
      { id: 7, text: "Mutual growth?", options: [{label: 'Encouraged', value: 3}, {label: 'Neutral', value: 2}, {label: 'Stagnant', value: 1}] },
      { id: 8, text: "Social circle impact?", options: [{label: 'Positive', value: 3}, {label: 'Neutral', value: 2}, {label: 'Negative', value: 1}] },
      { id: 9, text: "Fun/Joy factor?", options: [{label: 'High', value: 3}, {label: 'Average', value: 2}, {label: 'Low', value: 1}] },
      { id: 10, text: "Commitment level?", options: [{label: 'Fully In', value: 3}, {label: 'Testing', value: 2}, {label: 'Hesitant', value: 1}] }
    ]
  },
  {
    id: 'family',
    name: 'Family',
    icon: '👨‍👩‍👧',
    description: 'Family responsibilities, personal life choices',
    questions: [
      { id: 1, text: "Impact on family time?", options: [{label: 'Positive', value: 3}, {label: 'Neutral', value: 2}, {label: 'Negative', value: 1}] },
      { id: 2, text: "Financial burden on family?", options: [{label: 'None', value: 3}, {label: 'Manageable', value: 2}, {label: 'Heavy', value: 1}] },
      { id: 3, text: "Alignment with family goals?", options: [{label: 'Perfect', value: 3}, {label: 'Partial', value: 2}, {label: 'None', value: 1}] },
      { id: 4, text: "Stress impact on home life?", options: [{label: 'Low', value: 3}, {label: 'Moderate', value: 2}, {label: 'High', value: 1}] },
      { id: 5, text: "Support from spouse/partner?", options: [{label: 'Full', value: 3}, {label: 'Partial', value: 2}, {label: 'Opposed', value: 1}] },
      { id: 6, text: "Future security for children?", options: [{label: 'Improved', value: 3}, {label: 'Same', value: 2}, {label: 'Riskier', value: 1}] },
      { id: 7, text: "Geographic stability?", options: [{label: 'Stable', value: 3}, {label: 'May move', value: 2}, {label: 'Frequent travel', value: 1}] },
      { id: 8, text: "Legacy building potential?", options: [{label: 'High', value: 3}, {label: 'Medium', value: 2}, {label: 'Low', value: 1}] },
      { id: 9, text: "Health impact on family members?", options: [{label: 'Better', value: 3}, {label: 'Neutral', value: 2}, {label: 'Worse', value: 1}] },
      { id: 10, text: "Personal fulfillment vs. Duty?", options: [{label: 'Balanced', value: 3}, {label: 'Duty-heavy', value: 2}, {label: 'Selfish', value: 1}] }
    ]
  },
  {
    id: 'health',
    name: 'Health',
    icon: '🏃‍♂️',
    description: 'Fitness, diet, medical-related decisions',
    questions: [
      { id: 1, text: "Long-term health benefit?", options: [{label: 'Significant', value: 3}, {label: 'Moderate', value: 2}, {label: 'Temporary', value: 1}] },
      { id: 2, text: "Ease of implementation?", options: [{label: 'Simple', value: 3}, {label: 'Moderate', value: 2}, {label: 'Difficult', value: 1}] },
      { id: 3, text: "Scientific backing?", options: [{label: 'Proven', value: 3}, {label: 'Anecdotal', value: 2}, {label: 'Experimental', value: 1}] },
      { id: 4, text: "Cost of maintenance?", options: [{label: 'Low', value: 3}, {label: 'Average', value: 2}, {label: 'High', value: 1}] },
      { id: 5, text: "Impact on energy levels?", options: [{label: 'Boosts', value: 3}, {label: 'Neutral', value: 2}, {label: 'Drains', value: 1}] },
      { id: 6, text: "Mental health impact?", options: [{label: 'Positive', value: 3}, {label: 'Neutral', value: 2}, {label: 'Stressful', value: 1}] },
      { id: 7, text: "Sustainability (Can you stick to it?)", options: [{label: 'Forever', value: 3}, {label: 'Few months', value: 2}, {label: 'Few weeks', value: 1}] },
      { id: 8, text: "Risk of injury/side effects?", options: [{label: 'None', value: 3}, {label: 'Low', value: 2}, {label: 'High', value: 1}] },
      { id: 9, text: "Social support for this change?", options: [{label: 'Strong', value: 3}, {label: 'Average', value: 2}, {label: 'None', value: 1}] },
      { id: 10, text: "Immediate results vs. Patience?", options: [{label: 'Fast', value: 3}, {label: 'Steady', value: 2}, {label: 'Very slow', value: 1}] }
    ]
  },
  {
    id: 'lifestyle',
    name: 'Lifestyle',
    icon: '🌍',
    description: 'Daily habits, living choices, routines',
    questions: [
      { id: 1, text: "Daily happiness impact?", options: [{label: 'High', value: 3}, {label: 'Moderate', value: 2}, {label: 'Low', value: 1}] },
      { id: 2, text: "Environmental impact?", options: [{label: 'Eco-friendly', value: 3}, {label: 'Neutral', value: 2}, {label: 'Negative', value: 1}] },
      { id: 3, text: "Social status impact?", options: [{label: 'Positive', value: 3}, {label: 'Neutral', value: 2}, {label: 'Irrelevant', value: 1}] },
      { id: 4, text: "Freedom/Flexibility?", options: [{label: 'Increases', value: 3}, {label: 'Same', value: 2}, {label: 'Decreases', value: 1}] },
      { id: 5, text: "Cost of living change?", options: [{label: 'Decreases', value: 3}, {label: 'Same', value: 2}, {label: 'Increases', value: 1}] },
      { id: 6, text: "Alignment with personal values?", options: [{label: 'Perfect', value: 3}, {label: 'Good', value: 2}, {label: 'Poor', value: 1}] },
      { id: 7, text: "Ease of routine integration?", options: [{label: 'Seamless', value: 3}, {label: 'Requires effort', value: 2}, {label: 'Disruptive', value: 1}] },
      { id: 8, text: "Travel opportunities?", options: [{label: 'More', value: 3}, {label: 'Same', value: 2}, {label: 'Less', value: 1}] },
      { id: 9, text: "Community/Social life?", options: [{label: 'Enriches', value: 3}, {label: 'Neutral', value: 2}, {label: 'Isolates', value: 1}] },
      { id: 10, text: "Long-term satisfaction?", options: [{label: 'High', value: 3}, {label: 'Moderate', value: 2}, {label: 'Low', value: 1}] }
    ]
  },
  {
    id: 'technology',
    name: 'Technology',
    icon: '💻',
    description: 'Choosing tools, software, devices',
    questions: [
      { id: 1, text: "Productivity boost?", options: [{label: 'Significant', value: 3}, {label: 'Moderate', value: 2}, {label: 'Minimal', value: 1}] },
      { id: 2, text: "Learning curve?", options: [{label: 'Easy', value: 3}, {label: 'Moderate', value: 2}, {label: 'Steep', value: 1}] },
      { id: 3, text: "Integration with existing tools?", options: [{label: 'Perfect', value: 3}, {label: 'Good', value: 2}, {label: 'Poor', value: 1}] },
      { id: 4, text: "Cost vs. Utility?", options: [{label: 'Great Value', value: 3}, {label: 'Fair', value: 2}, {label: 'Overpriced', value: 1}] },
      { id: 5, text: "Future-proofing/Longevity?", options: [{label: 'High', value: 3}, {label: 'Moderate', value: 2}, {label: 'Short-lived', value: 1}] },
      { id: 6, text: "Security/Privacy?", options: [{label: 'Excellent', value: 3}, {label: 'Average', value: 2}, {label: 'Weak', value: 1}] },
      { id: 7, text: "Support/Community?", options: [{label: 'Strong', value: 3}, {label: 'Average', value: 2}, {label: 'None', value: 1}] },
      { id: 8, text: "Customization options?", options: [{label: 'Highly', value: 3}, {label: 'Some', value: 2}, {label: 'None', value: 1}] },
      { id: 9, text: "Reliability/Uptime?", options: [{label: '99.9%', value: 3}, {label: 'Average', value: 2}, {label: 'Buggy', value: 1}] },
      { id: 10, text: "Personal joy from using it?", options: [{label: 'High', value: 3}, {label: 'Neutral', value: 2}, {label: 'Frustrating', value: 1}] }
    ]
  },
  {
    id: 'personal_growth',
    name: 'Personal Growth',
    icon: '🌱',
    description: 'Self-improvement, mindset, discipline',
    questions: [
      { id: 1, text: "Confidence boost?", options: [{label: 'Significant', value: 3}, {label: 'Moderate', value: 2}, {label: 'Minimal', value: 1}] },
      { id: 2, text: "Discipline requirement?", options: [{label: 'High', value: 3}, {label: 'Moderate', value: 2}, {label: 'Low', value: 1}] },
      { id: 3, text: "Alignment with core purpose?", options: [{label: 'Perfect', value: 3}, {label: 'Good', value: 2}, {label: 'Vague', value: 1}] },
      { id: 4, text: "Comfort zone expansion?", options: [{label: 'Significant', value: 3}, {label: 'Some', value: 2}, {label: 'Safe', value: 1}] },
      { id: 5, text: "Long-term character impact?", options: [{label: 'Transformative', value: 3}, {label: 'Positive', value: 2}, {label: 'Neutral', value: 1}] },
      { id: 6, text: "Mental clarity impact?", options: [{label: 'Clears fog', value: 3}, {label: 'Neutral', value: 2}, {label: 'Confusing', value: 1}] },
      { id: 7, text: "Habit formation potential?", options: [{label: 'High', value: 3}, {label: 'Moderate', value: 2}, {label: 'Low', value: 1}] },
      { id: 8, text: "Overcoming fears?", options: [{label: 'Directly', value: 3}, {label: 'Somewhat', value: 2}, {label: 'Avoids', value: 1}] },
      { id: 9, text: "Inspiration to others?", options: [{label: 'High', value: 3}, {label: 'Moderate', value: 2}, {label: 'Low', value: 1}] },
      { id: 10, text: "Overall life satisfaction?", options: [{label: 'Increases', value: 3}, {label: 'Same', value: 2}, {label: 'Decreases', value: 1}] }
    ]
  }
];
