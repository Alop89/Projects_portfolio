#!/bin/bash

# 1. Crear directorios principales (usando llaves para eficiencia)
echo "📁 Creando estructura de carpetas..."
mkdir -p data/{raw,processed,external}
mkdir -p notebooks
mkdir -p src/{data,features,models,visualization,webapp}
mkdir -p tests
mkdir -p reports/figures

# 2. Agregar .gitkeep a todas las carpetas vacías
# Esto busca todos los directorios y crea el archivo si no existe
find . -type d -not -path '*/.*' -exec touch {}/.gitkeep \;
echo "📌 Archivos .gitkeep generados."

# 3. Crear .gitignore con estándares de Ciencia de Datos
echo "🛡️ Configurando .gitignore..."
cat <<EOT > .gitignore
# Datos y Bases de Datos
*.db
*.sqlite
*.csv
*.xlsx
*.pkl
*.pdf
*.docx
data/

# Entornos y Seguridad
venv/
.env
.DS_Store

# Notebooks y Python
__pycache__/
.ipynb_checkpoints/
EOT

# 4. Archivos iniciales de documentación
touch README.md
echo "Estructura del proyecto" > structure.txt
tree . >> structure.txt 2>/dev/null || ls -R >> structure.txt

# 5. Operaciones de Git (Solo si el repo ya está configurado)
echo "⬆️ Sincronizando con GitHub..."
git add .
git commit -m "Estructura inicial de repositorio"
git push origin main

echo "✅ ¡Proyecto listo y estructurado con éxito!"