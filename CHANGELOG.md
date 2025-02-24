# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog][keepachangelog-site],
and this project adheres to [Semantic Versioning][semver-site].

## [Unreleased]

### Added

- The `logs-slack-alerts` example. [#13]

## [1.0.0] - 2019-07-30

### Changed

- Supported version of Terraform is 0.12. [#11]

## [0.4.1] - 2019-07-03

### Fixed

- Project and region are applied to the scheduler job. [#8]

## [0.4.0] - 2019-06-17

### Added

- A variable which configures the time zone of the scheduler job. [#5]

## [0.3.0] - 2019-06-11

### Added

- Submodule which cleans up old projects.

## [0.2.0] - 2019-04-02

### Added

- Ability to specify a service account for functions to run as

## [0.1.0] - 2019-03-14

### Added

- Initial release

[Unreleased]: https://github.com/terraform-google-modules/terraform-google-scheduled-function/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/terraform-google-modules/terraform-google-scheduled-function/compare/v0.4.1...v1.0.0
[0.4.1]: https://github.com/terraform-google-modules/terraform-google-scheduled-function/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/terraform-google-modules/terraform-google-scheduled-function/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/terraform-google-modules/terraform-google-scheduled-function/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/terraform-google-modules/terraform-google-scheduled-function/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/terraform-google-modules/terraform-google-scheduled-function/releases/tag/v0.1.0

[#13]: https://github.com/terraform-google-modules/terraform-google-scheduled-function/pull/13
[#11]: https://github.com/terraform-google-modules/terraform-google-scheduled-function/pull/11
[#8]: https://github.com/terraform-google-modules/terraform-google-scheduled-function/pull/8
[#5]: https://github.com/terraform-google-modules/terraform-google-scheduled-function/pull/5

[keepachangelog-site]: https://keepachangelog.com/en/1.0.0/
[semver-site]: https://semver.org/spec/v2.0.0.html
