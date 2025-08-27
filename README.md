# HTAN Phase 2 Data Model (HTAN2)

---

## ⚠️ **DO NOT USE – UNDER DEVELOPMENT** ⚠️  

This data model is in **active development**. It builds on **HTAN Phase 1** and incorporates input from the **Cancer Data Standards (CDS)** initiative. Expect frequent changes until a stable version is released.

---

## Overview 

This repository is part of ongoing efforts to refine and standardize the HTAN2 data model. 

## 🏗️ Data Model Architecture

The HTAN2 data model is built using **LinkML**, a modeling language for schemas that generates Python data model classes and JSON schemas. The model follows a modular architecture with clear separation of concerns:

### **Core Module**
- **Purpose**: Universal attributes shared across all file-based modules
- **Location**: `modules/Core/domains/core.yaml`
- **Key Features**: 
  - Single primary key definition (`HTAN_DATA_FILE_ID`)
  - Required field definitions for relationships
  - HTAN identifier validation patterns
  - Base class for inheritance (`CoreFileAttributes`)

### **Biospecimen Module**
- **Purpose**: Base class for modules requiring biospecimen identification
- **Location**: `modules/Biospecimen/`
- **Key Features**: 
  - Required `HTAN_BIOSPECIMEN_ID` for biospecimen-based modules
  - Inherits from `CoreFileAttributes`

### **Participant Module**
- **Purpose**: Base class for modules requiring participant identification
- **Location**: `modules/Participant/`
- **Key Features**: 
  - Required `HTAN_PARTICIPANT_ID` for participant-based modules
  - Inherits from `CoreFileAttributes`

### **Sequencing Module**
- **Purpose**: Base class for all sequencing data types
- **Location**: `modules/Sequencing/`
- **Key Features**: 
  - Common sequencing attributes (LIBRARY_LAYOUT, SEQUENCING_PLATFORM, etc.)
  - Inherits from `BiospecimenAttributes`
  - Shared enums for sequencing platforms and library layouts

### **WES Module**
- **Purpose**: Bulk Whole Exome Sequencing data
- **Location**: `modules/WES/`
- **Structure**: Three processing levels (Level 1, 2, 3)
- **Features**: Sequencing platform enums, quality metrics, variant calling
- **Inheritance**: `WES → BaseSequencingAttributes → BiospecimenAttributes → CoreFileAttributes`

### **scRNA-seq Module**
- **Purpose**: Single-cell RNA Sequencing data
- **Location**: `modules/scRNA-seq/`
- **Structure**: Three processing levels (Level 1, 2, 3_4 combined)
- **Features**: h5ad file format validation, AnnData 0.1 schema compliance
- **Inheritance**: `scRNA-seq → BaseSequencingAttributes → BiospecimenAttributes → CoreFileAttributes`

### **Clinical Module**
- **Purpose**: Clinical and demographic data
- **Location**: `modules/Clinical/`
- **Structure**: Multiple domain files (demographics, diagnosis, therapy, etc.)
- **Features**: Comprehensive validation rules and conditional requirements
- **Inheritance**: `Clinical → ParticipantAttributes → CoreFileAttributes`

## 📁 Project Structure

```
htan-linkml/
├── modules/                    # All data model modules
│   ├── Core/                  # Universal attributes
│   ├── Biospecimen/           # Biospecimen base class
│   ├── Participant/           # Participant base class
│   ├── Sequencing/            # Base sequencing attributes
│   ├── WES/                   # Whole Exome Sequencing
│   ├── scRNA-seq/             # Single-cell RNA Sequencing
│   └── Clinical/              # Clinical data domains
├── config/                    # LinkML configuration
├── scripts/                   # Utility scripts
├── tests/                     # Root-level tests
└── docs/                      # Documentation
```

## 🔗 Key Relationships

### **Data Hierarchy**
```
Participant (HTAN_PARTICIPANT_ID)
├── Biospecimen (HTAN_BIOSPECIMEN_ID)
│   └── Level 1 Data (HTAN_DATA_FILE_ID) → HTAN_PARENT_ID: _B####
│       └── Level 2 Data (HTAN_DATA_FILE_ID) → HTAN_PARENT_ID: _D####
│           └── Level 3 Data (HTAN_DATA_FILE_ID) → HTAN_PARENT_ID: _D####
```

### **Primary Keys**
- `HTAN_DATA_FILE_ID`: Unique identifier for data files across all levels

### **Module-Specific Required Fields**
- `HTAN_PARTICIPANT_ID`: Required in participant-based modules (Clinical)
- `HTAN_BIOSPECIMEN_ID`: Required in biospecimen-based modules (WES, scRNA-seq)

### **Foreign Keys**
- `HTAN_PARENT_ID`: References parent entity using suffix convention
  - `_B####` - References a biospecimen
  - `_D####` - References a data file

## 🚀 Getting Started

### **Prerequisites**
- Python 3.11+
- Poetry (dependency management)
- LinkML tools

### **Installation**
```bash
# Clone the repository
git clone <repository-url>
cd htan-linkml

# Install dependencies
poetry install

# Generate schemas
make modules-gen

# Run tests
make test
```

## 📚 Module-Specific Documentation

Each module contains detailed documentation:

- **Core Module**: See `modules/Core/README.md` for primary/foreign key definitions
- **Clinical Module**: See `modules/Clinical/README.md` for domain descriptions
- **WES Module**: See `modules/WES/README.md` for sequencing levels

## 🤝 Contributing

For detailed contribution guidelines, development conventions, and step-by-step instructions for adding new modules, see **[CONTRIBUTING.md](CONTRIBUTING.md)**.

### **Quick Start for Contributors**
1. Fork the repository
2. Create feature branch: `git checkout -b feat/[module-name]`
3. Follow conventions in CONTRIBUTING.md
4. Run tests: `make test`
5. Submit pull request

## 📖 Additional Resources

- **LinkML Documentation**: [https://linkml.io/](https://linkml.io/)
- **HTAN Phase 1 (archived)**: [https://github.com/ncihtan/data-models](https://github.com/ncihtan/data-models)
- **Cancer Data Standards**: [https://cancer.gov/cancer-data-standards](https://cancer.gov/cancer-data-standards)


