# Gentleman Ecosystem

Repositorio central y orquestador del stack de **Gentle AI**, submódulos del ecosistema, configuración de Antigravity y colección de skills para agentes de Inteligencia Artificial.

## Estructura del Ecosistema

- **`skills/`**: Colección completa de skills curadas y activas (Suite Replica, Frontend, Arquitectura, SDD, Calidad).
- **`antigravity/`**: Plantillas de configuración (`mcp_config.example.json`) y guías de entorno.
- **Submódulos**:
  - `gentle-ai`: Framework core y CLI.
  - `engram`: Sistema de memoria persistente para agentes.
  - `agent-teams-lite`: Motor de Spec-Driven Development (SDD) y revisión adversarial.
  - `Gentleman-Skills`: Catálogo comunitario y curado de skills.
  - `gentleman-guardian-angel`: Guardián de seguridad y calidad.
  - `Gentleman.Dots`: Configuraciones de terminal, dotfiles y utilidades.
  - `Gentleman-MCP`: Servidor MCP oficial de Gentleman Programming.
  - `gentle-agent-state`: Máquina de estados de agentes.
  - `Gentleman-Terminal`: TUI y emulador de terminal avanzado.
  - `gentle-shell`: Shell agentic nativo de Pi.
  - `gentle-shell-desktop`: Aplicación desktop para Gentle Shell.

---

## Cómo replicar todo en una PC nueva

### 1. Clonar el repositorio con todos los submódulos
```bash
git clone --recurse-submodules https://github.com/dtl-tp/Gentleman-Ecosystem.git
cd Gentleman-Ecosystem
```

### 2. Sincronizar todas las skills a Antigravity
Ejecutar el script de sincronización desde PowerShell:
```powershell
.\sync-skills.ps1
```
> **Tip:** Si querés que los cambios en la carpeta de este repo se reflejen directamente sin tener que volver a copiar, pasale el flag `-Symlink`:
> ```powershell
> .\sync-skills.ps1 -Symlink
> ```

### 3. Configurar tus credenciales de MCP
El script creará automáticamente `%USERPROFILE%\.gemini\config\mcp_config.json` a partir de la plantilla si no existe. Solo tenés que abrirlo y colocar tus API keys (GitHub PAT, Google API Key, etc.).
