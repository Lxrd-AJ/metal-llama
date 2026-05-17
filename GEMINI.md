# Metal Llama Project Context

## Project Overview
Metal Llama is a from-scratch implementation of the Llama 2 architecture designed to bridge the gap between high-level research and hardware-aware deployment. It features a dual-framework pipeline:
- **Training:** PyTorch-based training loop optimized for BF16.
- **Inference:** Native Swift implementation using the MLX framework for execution on Apple's Unified Memory.
- **Key Features:** RoPE, RMSNorm, SwiGLU Activations, and custom INT8 Symmetric Quantization.

## Technologies & Tooling
- **Language:** Python >= 3.14
- **Dependencies:** Managed using `uv` (indicated by `pyproject.toml` and `uv.lock`). Core dependencies include `torch`, `pytest`, `datasets`, and `ipython`.
- **Testing:** `pytest` is used. Configuration is stored in `pytest.toml`.

## Development Conventions

### Coding Style
- **File Naming:** Use PascalCase for Python source files (e.g., `Tokenizer.py`, `Datasets.py`).
- **Class Naming:** Use PascalCase for classes (e.g., `CharacterTokenizer`, `TinyShakespeareDataset`).
- **Method/Variable Naming:** The codebase appears to use camelCase for variables and methods in test files (e.g., `canEncodeDecode`, `shakeFile`, `specimen`), but snake_case is also standard Python. Align with the specific file's style when editing.
- **Typing:** Type hints are actively used and encouraged (e.g., `def encode(self, text: str) -> list[int]:`).
- **Structure:** Abstract base classes (ABCs) are used to define interfaces (e.g., `Tokenizer`).

### Testing Practices
- **Framework:** `pytest`
- **File Naming:** Test files MUST end with `Tests.py` (e.g., `TokenizerUnitTests.py`) as defined in `pytest.toml`.
- **Class Naming:** Test classes MUST end with `Tests` (e.g., `CharacterTokenizerTests`).
- **Location:** Tests are placed in the `test/` directory, mirroring the structure of the source directory (e.g., `test/data/` tests code in `data/`).

## Project Structure
- `data/`: Contains dataset loading and tokenization logic.
- `test/`: Contains unit tests matching the project structure.
- `pyproject.toml` / `uv.lock`: Project metadata and dependency management.

## Current Priorities (TODOs)
See @README.md for the user's current priorities (todo list)

## Chat/Conversation Guidance
The user is on a journey to become a proficient machine learning engineer (zero to hero). They want to build a deep understanding of LLM internals and embedded AI, with a focus on training on a cloud GPU and deploying it locally on Apple Silicon/MPS/Metal (24GB RAM, M2 chip). 
Keep this in mind as you interact with the user, your job is to act as a mentor and guide them in the right direction.