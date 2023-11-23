#!/bin/bash

# Controlla se Python3 e pip sono installati
if ! command -v python3 &> /dev/null || ! command -v pip &> /dev/null; then
    echo "Python3 o pip non sono installati."
    exit 1
fi

# Controlla se le librerie di pip sono installate
pip_packages=("libreria1" "libreria2")  # Sostituisci con i nomi delle tue librerie
missing_packages=()
for package in "${pip_packages[@]}"; do
    if ! pip show "$package" &> /dev/null; then
        missing_packages+=("$package")
    fi
done

# Se ci sono pacchetti mancanti, chiedi all'utente se desidera installarli
if [ ${#missing_packages[@]} -gt 0 ]; then
    echo "I seguenti pacchetti sono mancanti: ${missing_packages[*]}"
    read -p "Desideri installarli? (S/n): " choice
    if [[ $choice == "S" || $choice == "s" ]]; then
        for package in "${missing_packages[@]}"; do
            echo "Installazione di $package..."
            pip install "$package"
        done
    else
        echo "Operazione annullata. Impossibile procedere senza i pacchetti necessari."
        exit 1
    fi
fi

# Chiedi all'utente l'URL del sito e un orario
read -p "Inserisci l'URL del sito: " sito
read -p "Inserisci un orario: " orario

# Esegui il file Python 'gestione' con i due argomenti precedenti
python3 gestione.py "$sito" "$orario"
