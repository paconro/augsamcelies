# Latvijas Dziesmas — Instrucciones de instalación

## ¿Qué es esto?
Una Progressive Web App (PWA) con las 238 canciones letonas del cancionero litúrgico.
Funciona offline en Android (y también en el navegador del ordenador).

---

## Instalación en Android

### Opción A — Servidor local con la app (recomendado)
Para funcionar como PWA instalable, el HTML necesita servirse desde HTTP/HTTPS
(no directamente desde un archivo). Las opciones más sencillas:

#### Con Termux (app gratuita en F-Droid):
```bash
pkg install nodejs
cd /ruta/a/dziesmas-app
npx serve .
```
Luego abre en Chrome: `http://localhost:3000`

#### Con una Raspberry Pi o servidor propio:
Copia la carpeta a cualquier servidor web (Apache, nginx, etc.)
y ábrela desde Chrome en el móvil.

#### Con GitHub Pages (gratuito, requiere cuenta GitHub):
1. Crea un repositorio público en GitHub
2. Sube los archivos de esta carpeta
3. Activa GitHub Pages en Settings → Pages
4. Abre la URL en Chrome Android

### Opción B — Instalación directa del APK (más sencillo)
Si quieres un APK instalable directamente sin servidor, podemos empaquetar
esta PWA con Bubblewrap o PWABuilder. Avísame y lo hacemos.

---

## Una vez abierta en Chrome:
1. Espera a que cargue la lista de canciones
2. Chrome mostrará automáticamente "Añadir a pantalla de inicio"
3. Si no aparece: menú ⋮ → "Añadir a pantalla de inicio"
4. La app se instala como una app nativa (sin barra de navegación)

---

## Funcionalidades offline
- ✅ Lista de canciones y búsqueda — siempre offline (datos incluidos)
- ✅ PDFs — se abren desde el servidor web la primera vez; después quedan en caché
- 🔄 Audio — se reproduce online; usa "Descargar para uso offline" por canción
- Los audios descargados se guardan en el dispositivo y funcionan sin internet

---

## Estructura de archivos
```
dziesmas-app/
├── index.html      — App principal
├── songs.json      — Datos de las 238 canciones
├── manifest.json   — Configuración PWA
├── sw.js           — Service Worker (cache offline)
├── icon-192.png    — Icono app
├── icon-512.png    — Icono app (grande)
└── README.md       — Este archivo
```

---

## Actualizar los datos
Para actualizar cuando cambies el Excel:
1. Ejecuta el script de conversión (pídelo si no lo tienes)
2. Reemplaza `songs.json` en el servidor
3. La app detectará el cambio automáticamente

---

## Soporte
Desarrollado con ♥ para la comunidad letona de Valencia.
