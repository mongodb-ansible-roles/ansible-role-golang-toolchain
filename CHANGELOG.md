# [1.6.0](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/compare/v1.5.0...v1.6.0) (2020-04-28)


### Features

* Add Archlinux support ([#15](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/issues/15)) ([a7122fa](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/a7122fab4699531c712ef42385815f7dbfc2c442))

# [1.5.0](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/compare/v1.4.0...v1.5.0) (2020-02-28)


### Bug Fixes

* Added missing requirements file to tests ([5f9ba82](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/5f9ba8258f5bf1456ed632d3a59c458512c4addf))
* Using shell command instead of copy/template ([d6c54de](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/d6c54de4d730f8009898bd7e13f5bbfbd6df02bd))


### Features

* Add s390x support ([47d8dc0](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/47d8dc0799fb684f0eb8449aa7d67efd502ada6d))

# [1.4.0](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/compare/v1.3.1...v1.4.0) (2020-02-27)


### Features

* Add rhel7 support ([a10adc9](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/a10adc952f53a35879dcc5cd78c1e3883bd2ac70))

## [1.3.1](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/compare/v1.3.0...v1.3.1) (2020-01-15)


### Bug Fixes

* Added context to test step in Circle ([8960996](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/89609962e2f2fa7c1eaa3e691d5947afa6d09426))
* Fixed spacing error in circle config ([3c996e6](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/3c996e69fdb4d19ddd2bd57979b4f383b9e49385))
* Install python3 when using dnf ([19746fa](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/19746fab7ed1be77092dc017aad272ead4616c50))
* Lint complains about using handlers ([33aabcb](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/33aabcbd03be856a51a4669078b0d8dee13bd9a0))
* Makefile needs environment variables for RHN ([9252b01](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/9252b01a94be153e293bc1f85d1b059e0cf07e2d))
* Replace missing header in yaml file ([772c551](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/772c551c4e7d9738c200ae772849bf2a7b1e4b73))


### Reverts

* Undo changes to make file ([3a8f0c3](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/3a8f0c358f139845f303715e8ef148b254afcd7b))

# [1.3.0](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/compare/v1.2.0...v1.3.0) (2020-01-14)


### Features

* Add RedHat support and PPC support ([52c751e](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/52c751e3be80de4537822375881b1ecca62070d0))

# [1.2.0](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/compare/v1.1.1...v1.2.0) (2019-11-06)


### Bug Fixes

* Add var to meta so vars are passed correctly ([26c6c95](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/26c6c952e8993467e000689e3f5909206caf0731))
* Changed golang dest variable name ([2486a8c](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/2486a8cd3fd222bcdeb89724647a27155793fc31))


### Features

* Added logic to move toolchain to correct dir ([5c65789](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/5c65789c4a972e9da4a241152549c235b87a00c7))
* Added toolchain_version file ([91e2216](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/91e2216789ce31babdaa982f09f1ea04885d8b98))

## [1.1.1](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/compare/v1.1.0...v1.1.1) (2019-08-29)


### Bug Fixes

* added golang prefix to variable ([4036e41](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/4036e41))

# [1.1.0](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/compare/v1.0.0...v1.1.0) (2019-08-24)


### Bug Fixes

* added destination to molecule playbook ([c35efc3](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/c35efc3))
* added vars to create toolchain url ([1628588](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/1628588))
* changed role to only set variable for subrole ([f109435](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/f109435))
* changed variable name to correct name ([8e3c2a2](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/8e3c2a2))
* moved dependencies block to correct location ([6d0dfb9](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/6d0dfb9))
* removed unused tasks ([5a6754a](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/5a6754a))


### Features

* added toolchain dependency role in meta ([ad8e950](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/ad8e950))
* added toolchain_dest variable ([008b030](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/008b030))

# 1.0.0 (2019-08-22)


### Bug Fixes

* added git again ([3a9e941](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/3a9e941))
* changed variable name for sha ([bf908ea](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/bf908ea))
* fix meta tag ([e33e613](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/e33e613))
* git required ([aaab748](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/aaab748))
* ignore swap files ([68b1061](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/68b1061))
* install git on container ([9751991](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/9751991))
* removed git dependency ([66de073](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/66de073))
* removed git from dockerfile ([dd983b9](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/dd983b9))
* removed git role ([ccc8d5c](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/ccc8d5c))
* removed unused variable ([1d32be6](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/1d32be6))
* task now uses toolchain role ([e29bb3d](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/e29bb3d))


### Features

* added darwin platforms ([be94c37](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/be94c37))
* added new golang toolchain ([d574dae](https://github.com/mongodb-ansible-roles/ansible-role-golang-toolchain/commit/d574dae))
