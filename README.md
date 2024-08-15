# API de Conversion de Fichiers

## Endpoints

### Convertir PDF en Texte

**POST** /convert/pdf-to-text/

- **Paramètre** : ile (PDF)
- **Réponse** : JSON avec le texte extrait

### Convertir Image en PDF

**POST** /convert/image-to-pdf/

- **Paramètre** : ile (Image JPEG ou PNG)
- **Réponse** : PDF

### Convertir PDF en Image

**POST** /convert/pdf-to-image/

- **Paramètre** : ile (PDF)
- **Réponse** : Image PNG
