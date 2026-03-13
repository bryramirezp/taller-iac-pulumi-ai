# Taller: Infraestructura como Código con Pulumi + AI

**Fecha:** 14 de marzo de 2026  
**Duración:** 45 minutos  
**Audiencia:** Estudiantes (nivel básico)  
**Lenguaje:** Python  
**Herramientas:** Pulumi CLI, AWS, OpenCode (AI)

---

## Objetivo del Taller

Demostrar de manera práctica cómo desplegar infraestructura real en AWS usando Pulumi (IaC) y acelerado con inteligencia artificial (OpenCode). El estudiante debe salir con la idea clara de que crear infraestructura en la nube ya no requiere interfaces gráficas ni conocimiento profundo de cada servicio: se puede hacer con código y con ayuda de AI.

---

## Estructura de la Charla (45 min)

### Bloque 1 — Teoría (10 min)

| Tiempo | Tema |
|--------|------|
| 0–3 min | ¿Qué es infraestructura tecnológica? (El iceberg: la capa invisible y el habilitador del negocio) |
| 3–6 min | ¿Qué es IaC y por qué importa? (el problema de hacer todo a mano en la consola) |
| 6–8 min | ¿Qué es Pulumi? (IaC con lenguajes reales: Python, TS, Go — diferencia con Terraform) |
| 8–10 min | AI + IaC (cómo OpenCode/Claude genera infraestructura desde lenguaje natural) |

### Bloque 2 — Demo: Website Estática en S3 (30 min)

| Tiempo | Tema |
|--------|------|
| 10–12 min | Setup del proyecto (`pulumi new aws-python`, estructura de archivos) |
| 12–25 min | Demo en vivo: usar OpenCode para generar el código del bucket S3 + upload del HTML + permisos públicos → `pulumi up` |
| 25–35 min | Revisión del código generado línea por línea + mostrar el sitio funcionando en el browser |
| 35–40 min | Momento "wow": modificar el HTML en vivo pidiéndoselo a OpenCode en lenguaje natural → `pulumi up` → ver el cambio reflejado |

### Bloque 3 — Cierre (5 min)

| Tiempo | Tema |
|--------|------|
| 40–42 min | Recapitulación: creamos infraestructura real sin tocar la consola de AWS |
| 42–43 min | `pulumi destroy` en vivo (cleanup y buenas prácticas de costos) |
| 43–45 min | Recursos para seguir aprendiendo + Q&A |

---

## Lo Que Vamos a Construir

### S3 Static Website

Un bucket S3 configurado como sitio web estático que sirve una página HTML pública.

**Recursos AWS que se crean:**
- `aws.s3.BucketV2` — el bucket
- `aws.s3.BucketWebsiteConfigurationV2` — habilita el hosting estático
- `aws.s3.BucketPublicAccessBlock` — permite acceso público
- `aws.s3.BucketOwnershipControls` — configura ownership
- `aws.s3.BucketAclV2` — ACL pública
- `aws.s3.BucketObject` — sube el `index.html`
- `aws.s3.BucketPolicy` — política de lectura pública

**Output esperado:**
```
website_url: http://<bucket-name>.s3-website-us-east-1.amazonaws.com
```

**Archivo `website/index.html`:** Página con diseño simple (HTML + CSS inline) con el tema del taller.

---

## Estructura de Archivos del Proyecto

```
pulumi_iac_aws/
│
├── PLAN.md                    # Este archivo: plan y documentación
├── README.md                  # Tutorial paso a paso para usar el proyecto
│
├── Pulumi.yaml                # Metadatos del proyecto Pulumi
├── Pulumi.dev.yaml            # Configuración del stack "dev"
├── __main__.py                # Código principal de Pulumi (toda la infra)
├── requirements.txt           # Dependencias Python (pulumi, pulumi-aws)
│
├── website/
│   └── index.html             # HTML del sitio estático
│
├── aws_free_tier.json         # Referencia de límites del Free Tier de AWS
│
└── slides/
    ├── outline.md             # Estructura y notas para la presentación
    ├── slide1.html            # Slide: ¿Qué es la infraestructura?
    ├── slide2.html            # Slide: ClickOps vs IaC
    ├── slide3.html            # Slide: ¿Qué es Pulumi?
    └── slide4.html            # Slide: AI + IaC
```

---

## Checklist de Construcción

### Setup inicial
- [x] Crear `requirements.txt` con dependencias de Pulumi
- [x] Crear `Pulumi.yaml` con metadatos del proyecto
- [x] Crear `Pulumi.dev.yaml` con config del stack dev

### Demo — S3 Website
- [x] Crear `website/index.html` con diseño atractivo del taller
- [x] Escribir código Pulumi en `__main__.py` para el bucket S3 website

### Material de la charla
- [x] Crear `slides/slide1.html` — ¿Qué es la infraestructura?
- [x] Crear `slides/slide2.html` — ClickOps vs IaC
- [x] Crear `slides/slide3.html` — ¿Qué es Pulumi?
- [x] Crear `slides/slide4.html` — AI + IaC
- [x] Crear `slides/outline.md` con la estructura completa de la presentación y notas del presentador

### Documentación
- [x] Crear `README.md` con tutorial paso a paso

---

## Pre-requisitos para el Día de la Charla

- [ ] Pulumi CLI instalado (`pulumi version`)
- [ ] AWS CLI instalado y configurado (`aws sts get-caller-identity`)
- [ ] Python 3.8+ instalado
- [ ] OpenCode instalado y funcionando
- [ ] Hacer un dry-run completo el día anterior
- [ ] Tener screenshots de backup por si algo falla en vivo
- [ ] Repositorio compartible con los estudiantes

---

## Recursos para Compartir con los Estudiantes

- [Pulumi Docs](https://www.pulumi.com/docs/)
- [Pulumi AWS Provider](https://www.pulumi.com/registry/packages/aws/)
- [OpenCode](https://opencode.ai)
- [AWS Free Tier](https://aws.amazon.com/free/)
- Este repositorio (link a compartir el día del taller)

---

## Notas Importantes

- **Costos:** S3 static website es prácticamente gratuito en el free tier de AWS. Siempre hacer `pulumi destroy` al finalizar.
- **Región:** Usar `us-east-1` por defecto para simplicidad.
- **Risk mitigation:** `pulumi up` puede tomar 30–90 segundos. Preparar screenshots del resultado esperado como plan B.
- **Demo incremental:** El `__main__.py` se construye incrementalmente durante la charla. Tener el código final listo como backup.
