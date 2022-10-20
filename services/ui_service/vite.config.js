import { resolve } from 'path';
import { defineConfig } from 'vite';
import solidPlugin from 'vite-plugin-solid';

const root = resolve(__dirname, 'src');
const outDir = resolve(__dirname, 'dist');

export default defineConfig({
  root: root,
  plugins: [solidPlugin()],
  server: {
    host: true,
    port: 5001,
    strictPort: true,
  },
  build: {
    outDir: outDir,
    emptyOutDir: true,
    rollupOptions: {
      input: {
        analyzer: resolve(root, 'analyzer', 'index.html'),
        login: resolve(root, 'auth', 'login', 'index.html'),
        signup: resolve(root, 'auth', 'signup', 'index.html'),
        profile: resolve(root, 'profile', 'index.html'),
        static: {
          images: resolve(root, 'assets', 'imgs'),
          js: resolve(root, 'assets', 'js'),
        }
      }
    },
    target: 'esnext',
  },
});
