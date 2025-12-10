import React, { useState, useEffect } from 'react';
import TextSelectionService from '../services/textSelectionService';

const ChatInterface = ({ sessionId, selectedText = null }) => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // If there's selected text, process it immediately
  useEffect(() => {
    if (selectedText) {
      processSelectedText(selectedText);
    }
  }, [selectedText]);

  // Function to process selected text
  const processSelectedText = async (text) => {
    setIsLoading(true);

    try {
      const response = await TextSelectionService.sendSelection(text, sessionId);

      // Add the response to messages
      setMessages(prev => [
        ...prev,
        { type: 'user', content: `"${text}"` },
        {
          type: 'assistant',
          content: response.response,
          sources: response.sources
        }
      ]);
    } catch (error) {
      console.error('Error processing selected text:', error);
      setMessages(prev => [
        ...prev,
        { type: 'user', content: `"${text}"` },
        { type: 'assistant', content: 'Sorry, I encountered an error processing the selected text.' }
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  // Function to send a message to the backend
  const sendMessage = async (query, context = null) => {
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/api/chatbot/query', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: query,
          context: context || {
            sessionId: sessionId || 'default-session'
          },
          options: {
            includeSources: true,
            maxSources: 3
          }
        })
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      const data = await response.json();

      // Add the response to messages
      setMessages(prev => [
        ...prev,
        { type: 'user', content: query },
        {
          type: 'assistant',
          content: data.response,
          sources: data.sources
        }
      ]);
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages(prev => [
        ...prev,
        { type: 'user', content: query },
        { type: 'assistant', content: 'Sorry, I encountered an error processing your request.' }
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputValue.trim() && !isLoading) {
      sendMessage(inputValue);
      setInputValue('');
    }
  };

  return (
    <div className="chat-interface">
      <div className="chat-header">
        Textbook AI Assistant
      </div>
      <div className="chat-messages">
        {messages.length === 0 ? (
          <p>Ask me anything about the textbook content!</p>
        ) : (
          messages.map((msg, index) => (
            <div key={index} className={`message ${msg.type}`}>
              <div className="message-content">
                {msg.content}
                {msg.sources && msg.sources.length > 0 && (
                  <div className="sources">
                    <small>Sources: {msg.sources.map(s => s.chapter_title).join(', ')}</small>
                  </div>
                )}
              </div>
            </div>
          ))
        )}
        {isLoading && <div className="loading">AI is thinking...</div>}
      </div>
      <form onSubmit={handleSubmit} className="chat-input-area">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Ask about the textbook..."
          className="chat-input"
          disabled={isLoading}
        />
        <button type="submit" className="chat-button" disabled={isLoading}>
          Send
        </button>
      </form>
    </div>
  );
};

export default ChatInterface;