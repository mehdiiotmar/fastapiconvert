# API de Conversion de Fichiers

## Endpoints

### Convertir PDF en Texte

**POST** /convert/pdf-to-text/

- **Param�tre** : ile (PDF)
- **R�ponse** : JSON avec le texte extrait

### Convertir Image en PDF

**POST** /convert/image-to-pdf/

- **Param�tre** : ile (Image JPEG ou PNG)
- **R�ponse** : PDF

### Convertir PDF en Image

**POST** /convert/pdf-to-image/

- **Param�tre** : ile (PDF)
- **R�ponse** : Image PNG
