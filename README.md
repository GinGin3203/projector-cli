# projector-cli

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**projector-cli** is a [**projector-installer**](https://github.com/JetBrains/projector-installer) port to Golang with
backward-compatible API and, possibly, incorporate

🚧 **<ins>projector-cli</ins> is alpha software in early stages of development. Also, unlike <ins>
projector-installer</ins>, this project is not backed by any commercial organization, so please do not expect the same
level of support as you may get with <ins>projector-installer</ins> on
the [official JetBrains issue tracker](https://youtrack.jetbrains.com/issues/PRJ)** 🚧

## Contents

- [Goals](#goals)
- [Why re-implement?](#why-re-implement)
- [Quick start](#quick-start)
- [Roadmap](#roadmap)
- [Contributing](#contributing)

## Goals

The main goal of the project is to implement a CLI tool that supports the same functionality with the same API as
**projector-installer**, but leveraging the benefits of using Golang.

The project will reach version v1.0 when *all* of **projector-installer** features will have been successfully (i.e.
without major issues) re-implemented.

Further features may include
[**projector-docker**](https://github.com/JetBrains/projector-docker) scripts functionality.

## Why re-implement?

- Having a snappier and faster CLI tool feels nice!
- A single binary is more convenient to distribute than multiple `.py` files
- [cobra](https://github.com/spf13/cobra), a CLI toolkit for Go, offers features like shell autocomplete and intelligent
  suggestions out-of-the-box. Analogous Python toolkits don't seem to match that. Also, performance

## Quick start

TODO

## Roadmap

TODO

## Contributing

All contributions are welcome!

Please, create an issue before submitting a pull request, if it's not a minor fix in docs or comments