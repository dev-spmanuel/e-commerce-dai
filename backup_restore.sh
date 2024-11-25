#!/bin/bash

# Variables
BACKUP_DATE="24-11-24"
BACKUP_DIR="/backups/$BACKUP_DATE"
DB_NAME="tienda"
IMAGES_DIR="/e-commerce/static/img"

# mongorestore --db tienda --drop ./backups/24-11-24/tienda/
mongorestore --uri="mongodb://mongo:27017" --db $DB_NAME --drop $BACKUP_DIR/$DB_NAME/

# Restaurar las imágenes
if [ -d "$BACKUP_DIR/img" ]; then
  rm -rf $IMAGES_DIR
  mkdir -p $IMAGES_DIR
  cp -r $BACKUP_DIR/img/* $IMAGES_DIR/
  echo "Imágenes restauradas correctamente."
else
  echo "No se encontraron imágenes para restaurar."
fi