import React, { useState } from 'react';
import { MessageCircle, X, Send } from 'lucide-react';
import { sendChatMessage } from '../lib/api';

const Chatbot = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { text: "Hello! I'm your Decision Assistant. How can I help you today?", sender: 'bot' }
  ]);
  const [input, setInput] = useState('');
  const [isSending, setIsSending] = useState(false);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim() || isSending) return;

    const message = input.trim();
    const newMessages = [...messages, { text: message, sender: 'user' }];
    setMessages(newMessages);
    setInput('');
    setIsSending(true);

    try {
      const data = await sendChatMessage(message);
      setMessages(prev => [...prev, { text: data.reply, sender: 'bot' }]);
    } catch (error) {
      setMessages(prev => [...prev, {
        text: error.message || 'The assistant is unavailable right now.',
        sender: 'bot'
      }]);
    } finally {
      setIsSending(false);
    }
  };

  return (
    <>
      <button className="chatbot-toggle" onClick={() => setIsOpen(!isOpen)}>
        {isOpen ? <X size={24} /> : <MessageCircle size={24} />}
      </button>

      {isOpen && (
        <div className="chatbot-window">
          <div className="chatbot-header">
            <span style={{ fontWeight: 700 }}>Decision Assistant</span>
            <X size={18} style={{ cursor: 'pointer' }} onClick={() => setIsOpen(false)} />
          </div>
          <div className="chatbot-messages">
            {messages.map((msg, i) => (
              <div key={i} className={`message ${msg.sender}`}>
                {msg.text}
              </div>
            ))}
          </div>
          <form className="chatbot-input" onSubmit={handleSend}>
            <input 
              type="text" 
              placeholder="Type a message..." 
              value={input}
              disabled={isSending}
              onChange={(e) => setInput(e.target.value)}
            />
            <button type="submit" className="btn-primary" style={{ padding: '0.5rem' }} disabled={isSending}>
              <Send size={18} />
            </button>
          </form>
        </div>
      )}
    </>
  );
};

export default Chatbot;
