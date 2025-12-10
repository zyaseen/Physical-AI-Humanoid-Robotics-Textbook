import React from 'react';
import Link from '@docusaurus/Link';

const TableOfContents = ({ chapters }) => {
  return (
    <div className="table-of-contents">
      <h2>Table of Contents</h2>
      <ul>
        {chapters.map((chapter, index) => (
          <li key={chapter.id}>
            <Link to={`/chapters/${chapter.slug}`}>
              {chapter.chapter_number}. {chapter.title}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TableOfContents;