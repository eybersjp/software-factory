# Contributing to Software Factory

First off, thank you for considering contributing to Software Factory! It's people like you that make Software Factory such a great tool.

## Where do I go from here?

If you've noticed a bug or have a feature request, please [submit an issue](issues) to the repository.

### Fork & create a branch

1. Fork the repo.
2. Clone your fork locally (`git clone git@github.com:YOUR_GITHUB_USERNAME/software-factory.git`).
3. Setup the workspace using `uv` environment (`uv sync`).
4. Create a new branch for your feature (`git checkout -b feature/my-new-feature`).

### Implementation Guidelines

* **Code Style:** Ensure you use standard Python typing.
* **Testing:** Since this architecture generates complex apps via prompts, ensure you include test outputs of your Prompts when updating `Prompt-OS`.

### Pull Requests

* Fill out the standard Pull Request template.
* Link any relevant issues.
* Ensure all tests pass.

By contributing to this repository, you agree that your contributions will be licensed under its MIT License.
