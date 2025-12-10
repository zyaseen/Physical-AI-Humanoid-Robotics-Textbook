import React from 'react';

const ChatResponse = ({ response, sources }) => {
  return (
    <div className="chat-response">
      <div className="response-content">
        {response}
      </div>
      {sources && sources.length > 0 && (
        <div className="response-sources">
          <h4>Sources:</h4>
          <ul>
            {sources.map((source, index) => (
              <li key={index}>
                <strong>{source.chapter_title}</strong> (Relevance: {(source.relevance * 100).toFixed(0)}%)
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default ChatResponse;