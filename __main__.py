"""
Taller: Infraestructura como Codigo con Pulumi + AI
Fecha: 14 de marzo de 2026
Lenguaje: Python | Provider: AWS | Region: us-east-1

Este archivo define la infraestructura del taller:
  - S3 Static Website (bucket publico con index.html)
"""

import json
import pulumi
import pulumi_aws as aws

# ---------------------------------------------------------------------------
# CONFIGURACION
# ---------------------------------------------------------------------------

stack = pulumi.get_stack()                  # "dev"
project = pulumi.get_project()              # "pulumi-iac-taller"

# Nombre base para todos los recursos (evita colisiones entre stacks)
nombre_base = f"{project}-{stack}"


# ===========================================================================
# S3 STATIC WEBSITE
# ===========================================================================
# Objetivo: crear un bucket S3 que sirva el archivo website/index.html
# como un sitio web publico accesible desde el browser.
# ===========================================================================

# 1. Crear el bucket S3
bucket = aws.s3.BucketV2(
    f"{nombre_base}-bucket",
    force_destroy=True,   # Permite destruirlo aunque tenga objetos (util en demos)
)

# 2. Deshabilitar el bloqueo de acceso publico
# (por defecto AWS bloquea todo acceso publico — hay que levantarlo explicitamente)
public_access_block = aws.s3.BucketPublicAccessBlock(
    f"{nombre_base}-public-access",
    bucket=bucket.id,
    block_public_acls=False,
    block_public_policy=False,
    ignore_public_acls=False,
    restrict_public_buckets=False,
)

# 3. Configurar el ownership del bucket (requerido antes de poder usar ACLs)
ownership_controls = aws.s3.BucketOwnershipControls(
    f"{nombre_base}-ownership",
    bucket=bucket.id,
    rule=aws.s3.BucketOwnershipControlsRuleArgs(
        object_ownership="BucketOwnerPreferred",
    ),
)

# 4. Configurar ACL publica (despues de los pasos 2 y 3)
bucket_acl = aws.s3.BucketAclV2(
    f"{nombre_base}-acl",
    bucket=bucket.id,
    acl="public-read",
    opts=pulumi.ResourceOptions(depends_on=[public_access_block, ownership_controls]),
)

# 5. Habilitar el hosting de sitio web estatico
website_config = aws.s3.BucketWebsiteConfigurationV2(
    f"{nombre_base}-website-config",
    bucket=bucket.id,
    index_document=aws.s3.BucketWebsiteConfigurationV2IndexDocumentArgs(
        suffix="index.html",
    ),
)

# 6. Subir el archivo index.html al bucket
index_html = aws.s3.BucketObject(
    "index.html",
    bucket=bucket.id,
    source=pulumi.FileAsset("website/index.html"),
    content_type="text/html",
    acl="public-read",
    opts=pulumi.ResourceOptions(depends_on=[bucket_acl]),
)

# 7. Politica de bucket: permite a cualquiera leer los objetos
bucket_policy = aws.s3.BucketPolicy(
    f"{nombre_base}-policy",
    bucket=bucket.id,
    policy=bucket.id.apply(
        lambda id: json.dumps({
            "Version": "2012-10-17",
            "Statement": [{
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{id}/*",
            }],
        })
    ),
    opts=pulumi.ResourceOptions(depends_on=[public_access_block]),
)

# Output: URL del sitio web estatico
website_url = website_config.website_endpoint.apply(
    lambda endpoint: f"http://{endpoint}"
)
pulumi.export("website_url", website_url)
