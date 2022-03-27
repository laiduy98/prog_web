# Programmation web project

## Members
- Zilu YANG
- LAI Khang Duy
- Mariia Klimina
- Nadia KACEM CHAOUCHE

## Environment setup

### Export environment

Install environment using conda
```
conda env create -f environment.yml
```

Type this in order to export the environment that you have
```
conda env export | grep -v "^prefix: " > environment.yml
```

## How to run

```
streamlit run src/app.py
```
