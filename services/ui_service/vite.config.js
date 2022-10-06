import { resolve } from 'path';
import { defineConfig } from 'vite';
import solidPlugin from 'vite-plugin-solid';

const root = resolve(__dirname, 'src');
const outDir = resolve(__dirname, 'dist');

export default defineConfig({
  root: root,
  plugins: [solidPlugin()],
  server: {
    port: 3000,
  },
  build: {
    outDir: outDir,
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: resolve(root, 'index.html'),
        login: resolve(root, 'login', 'index.html'),
        signup: resolve(root, 'signup', 'index.html'),
      }
    },
    target: 'esnext',
  },
});
