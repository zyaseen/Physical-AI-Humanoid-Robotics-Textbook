import React from 'react';
import TextSelection from './TextSelection';

const Chapter = ({ title, content, onTextSelect }) => {
  return (
    <div className="chapter-container">
      <h1>{title}</h1>
      <div className="chapter-content">
        {content && content.split('\n\n').map((paragraph, index) => (
          <p key={index}>{paragraph}</p>
        ))}
      </div>
      <TextSelection onTextSelect={onTextSelect} />
    </div>
  );
};

export default Chapter;