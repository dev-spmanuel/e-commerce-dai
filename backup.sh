#!/bin/bash

# Variables
BACKUP_DATE=$(date +%d-%m-%y)
BACKUP_DIR="./backups/$BACKUP_DATE"
DB_NAME="tienda"
IMAGES_DIR="./e-commerce/static/img"

# Crear directorio de backup
mkdir -p $BACKUP_DIR

# mongodump --db tienda --out ./backups/`date +"%m-%d-%y"`
mongodump --db $DB_NAME --out $BACKUP_DIR

# Hacer backup de las imágenes
cp -r $IMAGES_DIR/* $BACKUP_DIR/img

echo "Backup completado en $BACKUP_DIR"