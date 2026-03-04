// Types
import type { App } from 'vue'
/**
 * plugins/index.ts
 *
 * Automatically included in `./src/main.ts`
 */

import router from '../router'

// Plugins
import vuetify from './vuetify'

export function registerPlugins (app: App) {
  app.use(vuetify)
  app.use(router)
}
