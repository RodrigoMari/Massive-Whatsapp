# Massive-Whatsapp

Este proyecto tiene como objetivo la entrega masiva de fotos via whatsapp con el uso de python. 

## Requisitos

Es necesario que tenga alguna versión de excel para poder editar el maestro. También es necesario tener todos los contactos y las fotos a enviar así como un Whatsapp con posibilidad de abrir Whatsapp Web con un QR.

## Uso

1. **Clonar el repositorio o descargar el ZIP**:

   Si no tenes Git, podes descargar el archivo ZIP desde GitHub.

   - Descargar ZIP desde GitHub: [Vcard Generator en GitHub](https://github.com/RodrigoMari/Vcard-generator)
   - O clona el repositorio usando Git:

     ```sh
     git clone https://github.com/RodrigoMari/Vcard-generator.git
     ```

2. **Navegar al directorio del proyecto**:

   Una vez descargado el proyecto, descomprima el archivo zip y entre a la carpeta

3. **Carga de datos**

   - En dicho directorio encontrará 2 cosas a editar:
    - Una carpeta en la que podrá subir las fotos a subir llamada "Fotos"
    - Un archivo llamado "Excel_contactos_fotos", metase y edite tanto el número al que lo quiere enviar (con el codigo de area y sin el 15) en la columna "Telefonos" como así el nombre (Fotos a enviar\nombre.jpg) en la columna "Foto" con el que subió la foto a la carpeta mencionada anteriormente. No se olvide de la extension (ej. .png o .jpg)

4. **Ejecutar archivo final**
   
   Dentro del directorio principal encontrará el archivo ejecutable llamado "Massive-setup.bat" al que deberá darle doble click. Este archivo reproduce varios pasos en consola, entre ellos descargar python, pip y las dependencias necesarias. No debe temer de dichas descargas ya que, ademas de ser aplicaciones de Microsoft, se ejecutan en un entorno virtual ajeno a su computadora (cuando termine sera borrado todo lo instalado)

   La instalacion tarda un par de minutos la primera vez, luego se ejecuta en pocos segundos

   [URGENTE] **Hay un error de descarga con python en el que luego de su descarga se cierra la consola, simplemente debe darle nuevamente doble click al ejecutable**

5. **Escanear QR**

   Se le abrirá una pestaña en la que le pedirá un QR para abrir su Whatsapp Web, este será el emisor de los mensajes. Acto seguido empezara a buscar y enviar los contactos y las fotos subidos anteriormente

## Recomendacion

Puede resultar que en una primera instancia es mas rápido enviarlas manualmente. Sin embargo el objetivo es que en el futuro cuando dichos contactos vuelvan a repetirse en sus envios usted solo suba las fotos a la carpeta con el nombre de la persona a enviar.

```
Telefono        Foto
3416584719      Fotos\Rodrigo.jpg
```

