import React, { useState, useEffect } from 'react';

const TextSelection = ({ onTextSelect }) => {
  const [selectedText, setSelectedText] = useState('');
  const [showPopup, setShowPopup] = useState(false);
  const [popupPosition, setPopupPosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const handleSelection = () => {
      const selectedText = window.getSelection().toString().trim();
      
      if (selectedText) {
        const selection = window.getSelection();
        if (selection.rangeCount > 0) {
          const range = selection.getRangeAt(0);
          const rect = range.getBoundingClientRect();
          setPopupPosition({ 
            x: rect.left + window.scrollX, 
            y: rect.top + window.scrollY - 40 // Position above the selection
          });
          setSelectedText(selectedText);
          setShowPopup(true);
        }
      } else {
        setShowPopup(false);
      }
    };

    document.addEventListener('mouseup', handleSelection);
    return () => {
      document.removeEventListener('mouseup', handleSelection);
    };
  }, []);

  const handleAskAI = () => {
    if (selectedText) {
      onTextSelect(selectedText);
      setShowPopup(false);
    }
  };

  return (
    <>
      {showPopup && (
        <div 
          className="selected-text-popup"
          style={{ 
            position: 'fixed', 
            left: popupPosition.x, 
            top: popupPosition.y,
            zIndex: 1000
          }}
          onClick={handleAskAI}
        >
          Ask AI
        </div>
      )}
    </>
  );
};

export default TextSelection;