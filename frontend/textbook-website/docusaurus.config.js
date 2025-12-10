const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

// With JSDoc @type annotations, IDEs can provide config autocompletion
/** @type {import('@docusaurus/types').DocusaurusConfig} */
(module.exports = {
  title: 'Physical AI & Humanoid Robotics Textbook',
  tagline: 'A comprehensive guide to Physical AI and Humanoid Robotics',
  url: 'https://physical-ai-humanoid-robotics-textbook-by-yaseen-it6jegmjg.vercel.app/', // Replace with your website's URL
  baseUrl: '/',
  trailingSlash: true, // This forces trailing slashes on all routes
         // ... rest of your config
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'textbook-org', // Your GitHub org/user name
  projectName: 'physical-ai-textbook', // Your repo name

  presets: [
    [
      '@docusaurus/preset-classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl: 'https://github.com/your-username/physical-ai-textbook/edit/main/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/your-username/physical-ai-textbook/edit/main/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Physical AI Textbook',
        logo: {
          alt: 'Physical AI & Humanoid Robotics Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'doc',
            docId: '1-introduction-to-physical-ai',
            position: 'left',
            label: 'Textbook',
          },
          {to: '/chapters', label: 'All Chapters', position: 'left'},
          {to: '/blog', label: 'Blog', position: 'left'},
          {
            href: 'https://github.com/your-username/physical-ai-textbook',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Textbook',
            items: [
              {
                label: 'Introduction to Physical AI',
                to: '/docs/1-introduction-to-physical-ai',
              },
              {
                label: 'Humanoid Robotics Basics',
                to: '/docs/2-basics-of-humanoid-robotics',
              },
              {
                label: 'ROS 2 Fundamentals',
                to: '/docs/3-ros-2-fundamentals',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Stack Overflow',
                href: 'https://stackoverflow.com/questions/tagged/physical-ai',
              },
              {
                label: 'Discord',
                href: 'https://discordapp.com/invite/physical-ai',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/physicalAI',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'Blog',
                to: '/blog',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/your-username/physical-ai-textbook',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics Textbook. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
});
