import React, { useState, useEffect } from 'react';
import Layout from '@theme/Layout';
import { useLocation } from '@docusaurus/router';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import ChatInterface from '../components/ChatInterface';

// This component wraps the standard DocPage to add the chat interface
function ChapterPageWrapper({ children }) {
  const location = useLocation();
  const { siteConfig } = useDocusaurusContext();
  const [sessionId, setSessionId] = useState(null);
  
  // Create a session when the component mounts
  useEffect(() => {
    const createSession = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/session/create', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            userAgent: navigator.userAgent
          })
        });
        
        if (response.ok) {
          const data = await response.json();
          setSessionId(data.sessionId);
        }
      } catch (error) {
        console.error('Error creating session:', error);
        // Use a fallback session ID
        setSessionId('fallback-session-' + Date.now());
      }
    };
    
    createSession();
  }, []);
  
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="Physical AI & Humanoid Robotics textbook with AI-powered learning support">
      <div style={{ display: 'flex' }}>
        <main style={{ flex: 1, padding: '20px' }}>
          {children}
        </main>
        <div style={{ width: '350px', position: 'fixed', right: '20px', top: '100px' }}>
          {sessionId && <ChatInterface sessionId={sessionId} />}
        </div>
      </div>
    </Layout>
  );
}

export default ChapterPageWrapper;