#!/bin/bash

# FORMATO: mongorestore --db tienda --drop ./backups/<fecha_backup>/tienda/

# Variables
BACKUP_DATE="24-11-24"
BACKUP_DIR="./backups/$BACKUP_DATE"
DB_NAME="tienda"
IMAGES_DIR="./e-commerce/static/img"

# mongorestore --db tienda --drop ./backups/01-09-24/tienda/
mongorestore --db $DB_NAME --drop $BACKUP_DIR/$DB_NAME/

# Restaurar las imágenes
if [ -d "$BACKUP_DIR/img" ]; then
  mkdir -p $IMAGES_DIR
  cp -r $BACKUP_DIR/img/* $IMAGES_DIR/
  echo "Imágenes restauradas correctamente."
else
  echo "No se encontraron imágenes para restaurar."
fi