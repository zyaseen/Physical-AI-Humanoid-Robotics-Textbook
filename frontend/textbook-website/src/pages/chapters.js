import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

function ChapterPage() {
  const { siteConfig } = useDocusaurusContext();
  
  return (
    <Layout
      title={`Chapters - ${siteConfig.title}`}
      description="Physical AI & Humanoid Robotics textbook chapters">
      <div className="container margin-vert--lg">
        <div className="row">
          <main className="col col--8 col--offset-2">
            <h1>Physical AI & Humanoid Robotics Textbook</h1>
            <p>
              Welcome to the comprehensive textbook on Physical AI and Humanoid Robotics. 
              This resource covers fundamental concepts to advanced implementations.
            </p>
            
            <h2>Table of Contents</h2>
            <ul>
              <li><Link to="/docs/1-introduction-to-physical-ai">1. Introduction to Physical AI</Link></li>
              <li><Link to="/docs/2-basics-of-humanoid-robotics">2. Basics of Humanoid Robotics</Link></li>
              <li><Link to="/docs/3-ros-2-fundamentals">3. ROS 2 Fundamentals</Link></li>
              <li><Link to="/docs/4-digital-twin-simulation">4. Digital Twin Simulation (Gazebo + Isaac)</Link></li>
              <li><Link to="/docs/5-vision-language-action-systems">5. Vision-Language-Action Systems</Link></li>
              <li><Link to="/docs/6-capstone-simple-ai-robot-pipeline">6. Capstone: Simple AI-Robot Pipeline</Link></li>
            </ul>
            
            <div style={{ marginTop: '2rem', padding: '1rem', backgroundColor: '#f0f8ff', borderRadius: '4px' }}>
              <h3>Interactive Learning Support</h3>
              <p>
                As you read through the textbook, you can select any text and ask our AI assistant 
                for clarifications using the "Ask AI" button that appears. This provides contextual 
                explanations based specifically on the textbook content.
              </p>
            </div>
          </main>
        </div>
      </div>
    </Layout>
  );
}

export default ChapterPage;