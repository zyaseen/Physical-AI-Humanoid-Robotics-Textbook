// Service for handling text selection operations in the frontend
class TextSelectionService {
  /**
   * Extract context around the selected text
   * @param {string} selectedText - The text that was selected
   * @param {string} fullContent - The full content of the chapter/section
   * @returns {object} An object containing the selected text and surrounding context
   */
  static extractContext(selectedText, fullContent) {
    if (!selectedText || !fullContent) {
      return {
        selectedText: selectedText || '',
        context: '',
        position: -1
      };
    }
    
    // Find the position of the selected text in the full content
    const position = fullContent.indexOf(selectedText);
    
    if (position === -1) {
      // If exact match not found, try a more flexible approach
      return this._extractContextFlexible(selectedText, fullContent);
    }
    
    // Extract some context before and after the selected text
    const contextStart = Math.max(0, position - 100); // 100 chars before
    const contextEnd = Math.min(fullContent.length, position + selectedText.length + 100); // 100 chars after
    
    const context = fullContent.substring(contextStart, contextEnd);
    
    return {
      selectedText: selectedText,
      context: context,
      position: position
    };
  }
  
  /**
   * Flexible context extraction when exact match fails
   * @private
   */
  static _extractContextFlexible(selectedText, fullContent) {
    // Simple approach: find the most similar segment
    const words = selectedText.split(/\s+/).filter(w => w.length > 3); // Get meaningful words
    
    if (words.length === 0) {
      return {
        selectedText: selectedText,
        context: fullContent.substring(0, 200),
        position: 0
      };
    }
    
    // Find the position of the first significant word
    for (const word of words) {
      const pos = fullContent.toLowerCase().indexOf(word.toLowerCase());
      if (pos !== -1) {
        const contextStart = Math.max(0, pos - 100);
        const contextEnd = Math.min(fullContent.length, pos + word.length + 100);
        const context = fullContent.substring(contextStart, contextEnd);
        
        return {
          selectedText: selectedText,
          context: context,
          position: pos
        };
      }
    }
    
    // Fallback: return the beginning of the content
    return {
      selectedText: selectedText,
      context: fullContent.substring(0, 200),
      position: 0
    };
  }
  
  /**
   * Send selected text to the backend API
   */
  static async sendSelection(selectedText, sessionId) {
    try {
      const response = await fetch('http://localhost:8000/api/chatbot/query-with-selection', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          selectedText: selectedText,
          session_id: sessionId
        })
      });
      
      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }
      
      return await response.json();
    } catch (error) {
      console.error('Error sending text selection to backend:', error);
      throw error;
    }
  }
}

export default TextSelectionService;