import React from 'react';
import { Trash2, Plus } from 'lucide-react';

const OptionInput = ({ options, onAdd, onRemove, onChange }) => {
  return (
    <div className="form-group">
      <label className="form-label">Options to Consider</label>
      {options.map((option, index) => (
        <div key={index} className="option-input-wrapper">
          <input
            type="text"
            className="form-input"
            placeholder={`Option ${index + 1}`}
            value={option}
            onChange={(e) => onChange(index, e.target.value)}
          />
          {options.length > 2 && (
            <button 
              type="button" 
              className="btn-secondary" 
              style={{ padding: '0.5rem', color: '#ef4444' }}
              onClick={() => onRemove(index)}
            >
              <Trash2 size={18} />
            </button>
          )}
        </div>
      ))}
      <button 
        type="button" 
        className="btn-secondary" 
        style={{ width: '100%', marginTop: '0.5rem', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}
        onClick={onAdd}
      >
        <Plus size={18} /> Add Option
      </button>
    </div>
  );
};

export default OptionInput;
