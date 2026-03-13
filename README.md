# Infraestructura como Codigo con Pulumi + AI

Proyecto del taller que demuestra como desplegar un **sitio web estatico en Amazon S3** usando [Pulumi](https://www.pulumi.com/) (Infraestructura como Codigo) y [OpenCode](https://opencode.ai) como asistente de inteligencia artificial.

**Sin tocar la consola de AWS. Todo desde la terminal, con Python.**

---

## Que hace este proyecto

Con un solo comando (`pulumi up`), se crean **7 recursos en AWS** que resultan en un sitio web publico:

```
Browser  -->  URL publica  -->  S3 Bucket (website mode)  -->  index.html
```

**Recursos creados:**

| # | Recurso AWS | Descripcion |
|---|-------------|-------------|
| 1 | `S3 BucketV2` | El bucket donde vive el sitio |
| 2 | `BucketPublicAccessBlock` | Permite acceso publico al bucket |
| 3 | `BucketOwnershipControls` | Configura el ownership de los objetos |
| 4 | `BucketAclV2` | ACL de lectura publica |
| 5 | `BucketWebsiteConfigurationV2` | Habilita el modo de sitio web estatico |
| 6 | `BucketObject` | Sube el archivo `index.html` al bucket |
| 7 | `BucketPolicy` | Politica que permite a cualquiera leer los objetos |

**Costo estimado:** $0.00 (dentro del [AWS Free Tier](https://aws.amazon.com/free/))

---

## Pre-requisitos

Antes de empezar, necesitas tener instalado:

| Herramienta | Version minima | Para que se usa |
|-------------|----------------|-----------------|
| [Python](https://www.python.org/downloads/) | 3.8+ | Lenguaje del proyecto Pulumi |
| [Node.js](https://nodejs.org/) | 18+ | Requerido para instalar OpenCode |
| [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) | v2 | Conectar con tu cuenta de AWS |
| [Pulumi CLI](https://www.pulumi.com/docs/iac/download-install/) | 3.x | Motor de Infraestructura como Codigo |
| [OpenCode](https://opencode.ai) | Ultima | Asistente AI para generar y modificar codigo |

Tambien necesitas una **cuenta de AWS**. Si no tienes una, puedes crear una en [aws.amazon.com/free](https://aws.amazon.com/free/) — incluye un Free Tier generoso que cubre todo lo que hace este proyecto.

---

## Instalacion paso a paso

### Paso 1: Instalar Python

Descarga Python desde [python.org/downloads](https://www.python.org/downloads/) e instalalo. Verifica que funcione:

```bash
python --version
# Debe mostrar Python 3.8 o superior
```

> En algunos sistemas el comando es `python3` en lugar de `python`.

---

### Paso 2: Instalar Node.js

OpenCode requiere Node.js. Descargalo desde [nodejs.org](https://nodejs.org/) (version LTS recomendada). Verifica:

```bash
node --version
# Debe mostrar v18 o superior
```

---

### Paso 3: Instalar Pulumi CLI

**macOS / Linux:**
```bash
curl -fsSL https://get.pulumi.com | sh
```

**Windows (con Chocolatey):**
```powershell
choco install pulumi
```

**Windows (con Winget):**
```powershell
winget install pulumi
```

Verifica que se instalo correctamente:
```bash
pulumi version
# Debe mostrar v3.x.x
```

> Mas opciones de instalacion en la [documentacion oficial de Pulumi](https://www.pulumi.com/docs/iac/download-install/).

---

### Paso 4: Instalar OpenCode

OpenCode es un agente de codigo con IA que funciona en la terminal. Se instala con npm (incluido con Node.js):

```bash
npm install -g opencode-ai
```

**Alternativas de instalacion:**

| Metodo | Comando |
|--------|---------|
| curl (macOS/Linux) | `curl -fsSL https://opencode.ai/install \| bash` |
| Homebrew (macOS/Linux) | `brew install anomalyco/tap/opencode` |
| Chocolatey (Windows) | `choco install opencode` |
| Scoop (Windows) | `scoop install opencode` |

Verifica que funcione:
```bash
opencode --version
```

**Configurar el proveedor de IA:**

Al abrir OpenCode por primera vez, necesitas configurar un proveedor de LLM. La forma mas sencilla es usar OpenCode Zen:

1. Ejecuta `opencode` en la terminal
2. Escribe el comando `/connect`
3. Selecciona "opencode" y sigue las instrucciones en [opencode.ai/auth](https://opencode.ai/auth)
4. Inicia sesion, agrega datos de facturacion, y copia tu API key
5. Pega tu API key en la terminal

> Tambien puedes usar otros proveedores como Anthropic, OpenAI, etc. Consulta la [documentacion de proveedores](https://opencode.ai/docs/providers/).

---

### Paso 5: Configurar AWS CLI

Necesitas credenciales de AWS (Access Key ID y Secret Access Key). Si no tienes unas, crealas desde la [consola de IAM de AWS](https://console.aws.amazon.com/iam/).

```bash
aws configure
```

Te pedira 4 datos:
```
AWS Access Key ID: [tu-access-key]
AWS Secret Access Key: [tu-secret-key]
Default region name: us-east-1
Default output format: json
```

Verifica que la conexion funciona:
```bash
aws sts get-caller-identity
```

Debes ver un JSON con tu Account ID, ARN y User ID. Si ves un error, revisa tus credenciales.

---

## Configurar el proyecto

### 1. Clonar el repositorio

```bash
git clone <URL-del-repositorio>
cd pulumi_iac_aws
```

### 2. Crear un entorno virtual de Python

```bash
# Crear el entorno virtual
python -m venv venv

# Activarlo
# En macOS/Linux:
source venv/bin/activate

# En Windows (cmd):
venv\Scripts\activate

# En Windows (PowerShell):
venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Esto instala `pulumi` y `pulumi-aws`, las unicas dos dependencias del proyecto.

---

## Inicializar Pulumi

### 1. Iniciar sesion en Pulumi

Pulumi necesita un lugar para guardar el estado de tu infraestructura. Tienes dos opciones:

**Opcion A: Pulumi Cloud (recomendado para principiantes)**
```bash
pulumi login
```
Esto abre el navegador para crear una cuenta gratuita en [app.pulumi.com](https://app.pulumi.com). El estado se guarda en la nube de Pulumi.

**Opcion B: Estado local (sin cuenta)**
```bash
pulumi login --local
```
El estado se guarda en un archivo local en tu maquina.

### 2. Inicializar el stack

```bash
pulumi stack init dev
```

Esto crea el stack `dev` con la configuracion de region `us-east-1` (definida en `Pulumi.dev.yaml`).

> Si el stack `dev` ya existe, usa `pulumi stack select dev` en su lugar.

---

## Desplegar la infraestructura

Este es el momento clave. Con un solo comando, Pulumi crea todos los recursos en AWS:

```bash
pulumi up
```

Pulumi te mostrara un **plan** (preview) de lo que va a crear:

```
Previewing update (dev):

     Type                               Name                        Plan
 +   pulumi:pulumi:Stack                pulumi-iac-taller-dev       create
 +   ├── aws:s3:BucketV2                ...-bucket                  create
 +   ├── aws:s3:BucketPublicAccessBlock ...-public-access            create
 +   ├── aws:s3:BucketOwnershipControls ...-ownership                create
 +   ├── aws:s3:BucketAclV2             ...-acl                     create
 +   ├── aws:s3:BucketWebsiteConfig...  ...-website-config           create
 +   ├── aws:s3:BucketObject             index.html                  create
 +   └── aws:s3:BucketPolicy            ...-policy                  create

Resources:
    + 8 to create

Do you want to perform this update? yes
```

Escribe `yes` y presiona Enter. Pulumi creara los recursos (~60 segundos).

Al terminar, veras el output:

```
Outputs:
    website_url: "http://<nombre-del-bucket>.s3-website-us-east-1.amazonaws.com"
```

### Verificar

Copia la URL del output y abrela en tu navegador. Deberias ver el sitio web del taller.

Tambien puedes obtener la URL con:
```bash
pulumi stack output website_url
```

---

## Limpiar recursos (importante)

Cuando termines, **elimina todos los recursos** para evitar costos en tu cuenta de AWS:

```bash
pulumi destroy
```

Pulumi te mostrara lo que va a eliminar. Escribe `yes` para confirmar.

```
Do you want to perform this destroy? yes
Destroying (dev):

     Type                               Name                        Status
 -   pulumi:pulumi:Stack                pulumi-iac-taller-dev       deleted
 -   ├── aws:s3:BucketPolicy            ...-policy                  deleted
 -   ├── aws:s3:BucketObject             index.html                  deleted
 ...

Resources:
    - 8 deleted
```

> Pulumi conoce el orden correcto de eliminacion. No tienes que preocuparte por dependencias entre recursos.

---

## Estructura del proyecto

```
pulumi_iac_aws/
│
├── __main__.py            # Codigo Pulumi: define toda la infraestructura
├── Pulumi.yaml            # Metadatos del proyecto (nombre, runtime)
├── Pulumi.dev.yaml        # Configuracion del stack dev (region: us-east-1)
├── requirements.txt       # Dependencias Python (pulumi, pulumi-aws)
│
├── website/
│   └── index.html         # Pagina HTML que se sube al bucket S3
│
├── aws_free_tier.json     # Referencia: limites del Free Tier de AWS
├── PLAN.md                # Plan y documentacion del taller
│
└── slides/                # Material visual de la presentacion
    ├── outline.md         # Estructura y notas del presentador
    ├── slide1.html        # ¿Que es la infraestructura?
    ├── slide2.html        # ClickOps vs IaC
    ├── slide3.html        # ¿Que es Pulumi?
    └── slide4.html        # AI + IaC
```

---

## Usando OpenCode con este proyecto

OpenCode es un asistente de IA que puede ayudarte a entender, modificar y extender este proyecto directamente desde la terminal.

### Abrir OpenCode en el proyecto

```bash
cd pulumi_iac_aws
opencode
```

### Ejemplos de cosas que puedes pedirle

- *"Explicame que hace el archivo __main__.py linea por linea"*
- *"Modifica el index.html para que tenga un fondo azul y un boton"*
- *"Agrega una funcion Lambda que devuelva un JSON con la fecha actual"*
- *"Que recursos de AWS se crean con este codigo?"*

Despues de que OpenCode haga cambios, simplemente ejecuta `pulumi up` para aplicarlos en AWS.

---

## Comandos utiles de Pulumi

| Comando | Que hace |
|---------|----------|
| `pulumi up` | Despliega o actualiza la infraestructura |
| `pulumi destroy` | Elimina todos los recursos creados |
| `pulumi preview` | Muestra que cambios se harian (sin aplicar) |
| `pulumi stack output` | Muestra los outputs (URLs, IDs, etc.) |
| `pulumi stack` | Muestra info del stack actual |
| `pulumi refresh` | Sincroniza el estado con lo que existe en AWS |

---

## Recursos adicionales

| Recurso | Link |
|---------|------|
| Documentacion de Pulumi | [pulumi.com/docs](https://www.pulumi.com/docs/) |
| Pulumi AWS Provider | [pulumi.com/registry/packages/aws](https://www.pulumi.com/registry/packages/aws/) |
| OpenCode | [opencode.ai](https://opencode.ai) |
| Documentacion de OpenCode | [opencode.ai/docs](https://opencode.ai/docs) |
| AWS Free Tier | [aws.amazon.com/free](https://aws.amazon.com/free/) |
| Python Pulumi SDK | [pulumi.com/docs/iac/languages-sdks/python](https://www.pulumi.com/docs/iac/languages-sdks/python/) |

---

## Troubleshooting

### `pulumi up` falla con error de credenciales
Verifica que AWS CLI esta configurado correctamente:
```bash
aws sts get-caller-identity
```
Si falla, ejecuta `aws configure` de nuevo con tus credenciales.

### `Import "pulumi" could not be resolved`
Asegurate de que tu entorno virtual esta activado y las dependencias estan instaladas:
```bash
source venv/bin/activate   # o venv\Scripts\activate en Windows
pip install -r requirements.txt
```

### El sitio web no carga en el browser
S3 static websites usan HTTP (no HTTPS). Asegurate de que la URL empieza con `http://` y no `https://`.

### `pulumi stack init` dice que el stack ya existe
Usa `pulumi stack select dev` en lugar de `pulumi stack init dev`.

---

*Taller: Infraestructura como Codigo con Pulumi + AI — 14 de marzo de 2026*
