# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a fork of Aider, the well-established AI pair programming tool that runs in the terminal. Aider allows developers to collaborate with LLMs to edit code in their local git repository. 

**The primary purpose of this fork is to add a "Thought Partner" mode** - a new chat mode that engages in Socratic-style questioning to help developers clarify their goals, constraints, and design decisions before any code is written.

## Common Development Commands

### Running Aider
```bash
# Run from source during development
python -m aider

# Install in development mode
pip install -e .
```

### Testing
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/basic/test_coder.py

# Run specific test
pytest tests/basic/test_coder.py::TestCoder::test_specific_case
```

### Linting
```bash
# Install flake8 (included in dev dependencies)
pip install -r requirements/requirements-dev.txt

# Run flake8 (configured in pyproject.toml)
flake8
```

### Development Setup
```bash
# Create virtual environment
python3 -m venv ../aider_venv
source ../aider_venv/bin/activate

# Install dependencies
pip install -e .
pip install -r requirements.txt
pip install -r requirements/requirements-dev.txt

# Optional: Install pre-commit hooks
pre-commit install
```

## High-Level Architecture

### Core Components

1. **Coders** (`aider/coders/`): Different AI coding assistants with specialized behaviors
   - `base_coder.py`: Base class for all coders
   - `ask_coder.py`: Q&A without file modifications
   - `architect_coder.py`: Two-phase reasoning + editing
   - **`thought_partner_coder.py`**: Our custom Socratic questioning mode (NEW)
   - Various edit format coders (editblock, udiff, wholefile, etc.)

2. **Main Entry Point** (`aider/main.py`): CLI initialization, argument parsing, and session management

3. **Commands** (`aider/commands.py`): Interactive command handling (e.g., `/add`, `/drop`, `/chat-mode`)

4. **LLM Integration** (`aider/llm.py`, `aider/models.py`): Model configuration and API communication

5. **Repository Management** (`aider/repo.py`, `aider/repomap.py`): Git integration and codebase mapping

6. **I/O Handling** (`aider/io.py`): Terminal interface and user interaction

### Key Patterns

- **Coder Inheritance**: All coders inherit from `Coder` base class
- **Prompt Templates**: Each coder has associated prompt files (e.g., `ask_prompts.py`)
- **Mode Switching**: `/chat-mode` command switches between different coder implementations
- **File Context**: Coders maintain lists of active files for editing context

### Thought Partner Mode Implementation

The new Thought Partner mode added in this fork:
- Triggered via `/thought-partner` or `/chat-mode thought-partner`
- Implemented in `thought_partner_coder.py` and `thought_partner_prompts.py`
- Inherits from base `Coder` class
- **Key difference from other modes**: Focuses exclusively on asking clarifying questions without generating code
- Helps surface user motivations, constraints, and edge cases before implementation
- Guides users through a structured dialog to establish clear requirements

### Testing Structure

- Tests located in `tests/` directory
- Organized by category: `basic/`, `browser/`, `help/`, `scrape/`
- Uses pytest framework
- Test configuration in `pytest.ini`

## Development Tips for Thought Partner Mode

1. When modifying the Thought Partner mode:
   - Primary files: `aider/coders/thought_partner_coder.py` and `aider/coders/thought_partner_prompts.py`
   - Ensure it maintains its non-coding, questioning behavior
   - Test the Socratic dialog flow thoroughly

2. To test Thought Partner mode:
   ```bash
   python -m aider
   /chat-mode thought-partner
   ```

3. Keep the fork synced with upstream Aider:
   ```bash
   git remote add upstream https://github.com/Aider-AI/aider.git
   git fetch upstream
   git merge upstream/main
   ```

4. When adding new prompts for Thought Partner mode, focus on:
   - Open-ended questions that explore "why" and "what if"
   - Questions that uncover constraints and edge cases
   - Avoiding premature solutioning

5. The project uses pre-commit hooks for code quality - ensure Thought Partner additions pass all checks