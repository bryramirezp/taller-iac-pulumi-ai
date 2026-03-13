# Slides: Taller Pulumi IaC + AI

**Fecha:** 14 de marzo de 2026 | **Duración:** 45 min | **Audiencia:** Estudiantes (nivel básico)

---

## Slide 1 — ¿Qué es Infraestructura? (2 min)

**Titulo:** ¿Qué es la Infraestructura Tecnológica?

**Contenido:**
- Diagrama del "iceberg": arriba el producto (sitio web / app móvil), abajo la infraestructura (servidores, redes, bases de datos)
- "La Capa Invisible" — nadie se da cuenta de que existe hasta que falla
- "El Habilitador del Negocio" — es el motor que permite operar, procesar pagos, conectar usuarios

**Archivo:** `slide1.html`

---

## Slide 2 — ¿Por qué te debería importar? (2 min) ← GANCHO EMOCIONAL

**Titulo:** ¿Por qué te debería importar?

**Subtitulo:** Esto no es solo para ingenieros senior de DevOps.

**Contenido (4 tarjetas):**
1. **Tu Carrera** — Las empresas buscan ingenieros que sepan desplegar, no solo programar. IaC es una de las habilidades más demandadas.
2. **Tus Proyectos** — Tu portafolio, tu tesis, tu startup. En internet hoy, sin pagar hosting. AWS Free Tier te da 12 meses gratis.
3. **Tu Diferenciador** — La mayoría de tus compañeros solo saben escribir código local. Tú vas a saber ponerlo en producción.
4. **Costo: $0** — Python + Pulumi + OpenCode + AWS Free Tier. Todo gratis. No necesitas inversión, solo curiosidad y 45 minutos.

**Frase de cierre:**
> "Después de esta charla, vas a poder publicar un sitio web real en AWS. Solo con Python."

**Archivo:** `slide2.html`

---

## Slide 3 — ClickOps vs IaC (2 min)

**Titulo:** ¿Por qué importa la Infraestructura como Código (IaC)?

**Contenido:**
- Columna izquierda: **ClickOps (El Caos Manual)** — lento, propenso a errores, imposible de replicar, sin historial
- Columna derecha: **IaC (La Solución Elegante)** — automatizado, auditable, 100% replicable, mejores prácticas de SW
- VS central como separador visual

**Archivo:** `slide3.html` (antes slide2)

---

## Slide 4 — ¿Qué es Pulumi? (3 min)

**Titulo:** ¿Qué es Pulumi?

**Subtitulo:** Infraestructura como Código usando lenguajes que ya conoces.

**Contenido:**
- Flujo en 3 pasos: Tu Código → Motor Pulumi → La Nube
- No necesitas aprender un lenguaje nuevo (como HCL)
- Soporta Python, TypeScript, Go, C#, Java

**Archivo:** `slide4.html` (antes slide3)

---

## Slide 5 — AI + IaC (2 min)

**Titulo:** Inteligencia Artificial + IaC

**Subtitulo:** Genera infraestructura desde lenguaje natural.

**Contenido (3 bloques):**
1. **Tu Idea** — Describes lo que necesitas en lenguaje natural ("Crea un bucket S3 público y súbele este index.html")
2. **OpenCode (IA)** — Interpreta tu intención, genera código y lo aplica. Sin buscar documentación.
3. **Código Listo** — Infraestructura definida en Python, lista para desplegar. `pulumi up` → 7 recursos → URL pública.

**Frase de cierre:**
> "La IA conoce la sintaxis. Tú te enfocas en la arquitectura."

**Archivo:** `slide5.html` (antes slide4)

---

## Slide 6 — Demo: Deploy en Vivo (transición a demo)

**Titulo:** Demo: Sitio Web en S3

**Subtitulo:** De código Python a un sitio web público en ~60 segundos.

**Contenido:**
- Pipeline horizontal: `__main__.py` → `pulumi up` → `AWS S3` → `URL Pública`
- Preview de código (editor oscuro con syntax highlighting)
- Stats: 7 recursos AWS, 1 comando, ~60 segundos

**Frase de cierre:**
> "Todo desde la terminal. Sin tocar la consola de AWS."

**Archivo:** `slide6.html` (antes slide5)

---

## Slide 7 — Demo: S3 Website (13 min) — EN VIVO

**Titulo:** Demo: Sitio web estático en S3

**Diagrama:**
```
Browser → URL pública → S3 Bucket (website mode) → index.html
```

**Lo que se crea:**
- Un bucket S3 con nombre único
- Configuración de website hosting
- Permisos públicos de lectura
- El archivo `website/index.html` subido al bucket

**Comandos en vivo:**
```bash
# Ver el HTML que vamos a subir
cat website/index.html

# Desplegar la infraestructura
pulumi up

# Copiar la URL del output y abrir en el browser
```

**Nota para el presentador:** Mientras `pulumi up` corre (30-60 seg), explicar qué está pasando: Pulumi consulta el state, calcula el "diff", llama a la API de AWS, espera confirmación de cada recurso.

---

## Slide 8 — Revisión Demo (5 min)

**Titulo:** ¿Qué acaba de pasar?

**Contenido:**
- Pulumi creó **7 recursos** en AWS con un solo comando
- El estado quedó guardado (en Pulumi Cloud o localmente)
- Si ejecutamos `pulumi up` de nuevo → "no changes" (idempotente)
- Si cambiamos el HTML y volvemos a ejecutar → actualiza solo ese objeto

**Mostrar en vivo:**
```bash
# Ver el estado actual
pulumi stack

# Ver los outputs
pulumi stack output
```

**Concepto clave:**
> "Pulumi sabe exactamente qué existe en AWS. No duplica recursos, no rompe lo que ya existe."

---

## Slide 9 — Momento "wow": modificar con AI (5 min) — EN VIVO

**Titulo:** El poder de AI + IaC

**Demostración en vivo con OpenCode:**

Pedirle a OpenCode en lenguaje natural:
> "Modifica el index.html para que incluya una sección con la fecha actual y un mensaje de bienvenida personalizado"

OpenCode modifica `website/index.html`, luego:
```bash
pulumi up
# Solo actualiza el objeto HTML (no recrea el bucket)
# Ver el cambio reflejado en el browser
```

**Punto clave a remarcar:**
> "Pulumi es inteligente: solo actualiza lo que cambió. No destruye y recrea todo."

---

## Slide 10 — Cleanup (1 min) — EN VIVO

**Titulo:** Buenas prácticas: limpiar recursos

```bash
pulumi destroy
# Confirmar con "yes"
# Pulumi elimina TODOS los recursos en orden correcto
```

**Por qué es importante:**
- Evita costos inesperados en AWS
- S3 es casi gratis, pero es buena práctica
- Pulumi conoce el orden correcto de eliminación (no borra el bucket si tiene objetos, etc.)

---

## Slide 11 — Recapitulación (2 min)

**Titulo:** ¿Qué aprendimos hoy?

**Lista:**
1. **IaC** = infraestructura definida como código → reproducible, versionable, automatizable
2. **Pulumi** = IaC con Python (y otros lenguajes), sin HCL ni YAML especiales
3. **AWS S3** = almacenamiento en la nube que puede servir sitios web estáticos
4. **AI + IaC** = OpenCode puede generar y modificar infraestructura desde lenguaje natural
5. **`pulumi up` / `pulumi destroy`** = desplegar y limpiar con un solo comando

**Lo que NO tocamos hoy:**
- La consola de AWS (ni una sola vez)
- YAML/JSON de CloudFormation
- Scripts de Bash complejos

---

## Slide 12 — Recursos para seguir (1 min)

**Titulo:** ¿Dónde seguir aprendiendo?

| Recurso | URL |
|---------|-----|
| Pulumi Docs | https://www.pulumi.com/docs/ |
| Pulumi AWS Provider | https://www.pulumi.com/registry/packages/aws/ |
| OpenCode | https://opencode.ai |
| AWS Free Tier | https://aws.amazon.com/free/ |
| Código de este taller | _(compartir link al repo)_ |

**Próximos pasos sugeridos:**
- Agregar una función Lambda con API Gateway al proyecto
- Desplegar una app con Docker usando AWS ECS
- Crear un pipeline de CI/CD que ejecute `pulumi up` automáticamente

---

## Notas del Presentador

### Antes del taller (día anterior)
- [ ] Hacer un dry-run completo del `pulumi up` y `pulumi destroy`
- [ ] Tomar screenshots del resultado final (plan B si algo falla en vivo)
- [ ] Verificar que OpenCode está funcionando con el modelo correcto
- [ ] Asegurarse de tener `pulumi login` activo

### Durante el taller
- **Slides 1-2:** Contexto y gancho emocional. Hacerlo conversacional, conectar con la audiencia.
- **Slides 3-5:** Conceptos técnicos (IaC, Pulumi, AI). No leer las slides — hablar con ejemplos.
- **Slide 6:** Transición a la demo. Dar el mapa mental de lo que van a ver.
- **Demo (slides 7-8):** Mostrar el código ANTES de ejecutar. Explicar cada bloque.
- **Slide 9:** El momento "wow". Tener la instrucción para OpenCode lista para copiar/pegar.
- **Si algo falla:** tener las screenshots listas. Decir: "En caso de error, así es lo que verían" y mostrar el screenshot.

### Tiempos críticos
- `pulumi up` completo: ~60 segundos
- `pulumi up` solo HTML update: ~10 segundos
- `pulumi destroy`: ~30 segundos

### Preguntas frecuentes esperadas
- **"¿Es seguro poner el bucket público?"** → Para una demo de taller sí. En producción se usa CloudFront + S3 privado.
- **"¿Cuánto cuesta?"** → $0 dentro del free tier. S3 tiene 5 GB gratis los primeros 12 meses.
- **"¿Y si ya tengo Terraform?"** → Pulumi puede importar recursos de Terraform. También hay `pulumi convert`.
- **"¿Puedo usar esto para mi proyecto de universidad?"** → Absolutamente. El free tier de AWS cubre casi cualquier proyecto académico.
