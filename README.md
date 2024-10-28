# htan-linkml

A LinkML data model for HTAN Phase 2

## Website

[https://ncihtan.github.io/htan-linkml](https://ncihtan.github.io/htan-linkml)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [htan_linkml](src/htan_linkml)
    * [schema](src/htan_linkml/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/htan_linkml/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).