# Contributing to Didi50

Thank you for your interest in contributing to **didi50**! We appreciate your time and effort in helping us improve this tool. Whether you're fixing a bug, improving documentation, or suggesting new features, your contributions are valuable to us.

Before you get started, please take a moment to review this guide to ensure a smooth and collaborative contribution process.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
  - [Setting Up the Project](#setting-up-the-project)
  - [Finding Issues to Work On](#finding-issues-to-work-on)
- [Making Changes](#making-changes)
  - [Creating a Branch](#creating-a-branch)
  - [Making Your Changes](#making-your-changes)
  - [Testing Your Changes](#testing-your-changes)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Code Review Process](#code-review-process)
- [License](#license)

---

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](./CODE_OF_CONDUCT.md). Please read it to ensure a respectful and inclusive environment for everyone.

---

## Getting Started

### Setting Up the Project

1. **Fork the Repository**: Start by forking the [didi50 repository](https://github.com/direnzii/didi50) to your GitHub account.
2. **Clone the Repository**: Clone your forked repository to your local machine:
   ```bash
   git clone https://github.com/YOUR_USERNAME/didi50.git
   cd didi50
   ```
3. **Set Up the Environment**: Ensure you have Python installed (preferably the latest version). You can install the project dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
4. **Verify the Setup**: Run the project locally to ensure everything is working as expected.

---

### Finding Issues to Work On

- Check the [Issues tab](https://github.com/direnzii/didi50/issues) for open issues labeled `good first issue` or `help wanted`. These are great starting points for new contributors.
- If you find an issue you'd like to work on, leave a comment to let us know. We’ll assign it to you or guide you further.

---

## Making Changes

### Creating a Branch

Before making changes, create a new branch for your work:
```bash
git checkout -b your-branch-name
```

### Making Your Changes

- Follow the project's coding style and conventions.
- Write clear and concise commit messages. For example:
  ```bash
  git commit -m "fix: resolve issue with proxy handling"
  ```
- If your changes are related to an issue, reference the issue number in your commit message:
  ```bash
  git commit -m "feat: add support for custom headers #123"
  ```

### Testing Your Changes

- Ensure your changes do not break existing functionality.
- If applicable, add new tests to cover your changes.
- Run the tests locally before submitting your pull request.

---

## Submitting a Pull Request

1. **Push Your Changes**: Push your branch to your forked repository:
   ```bash
   git push origin your-branch-name
   ```
2. **Create a Pull Request**:
   - Go to the [didi50 repository](https://github.com/Direnzii/didi50) on GitHub.
   - Click on **New Pull Request** and select your branch.
   - Fill out the pull request template, providing details about your changes.
3. **Link to an Issue**: If your PR addresses an issue, link it using keywords like `closes #123` or `fixes #123`.

---

## Code Review Process

- A maintainer will review your pull request and provide feedback.
- Be responsive to any requested changes or questions.
- Once approved, your changes will be merged into the main branch.

---

## License

By contributing to **didi50**, you agree that your contributions will be licensed under the [MIT License](./LICENSE.txt).

---

Thank you for contributing to **didi50**! Your efforts help make this tool better for everyone. If you have any questions, feel free to reach out by opening an issue or contacting the maintainers.

---
